import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# landing directory
@app.route("/")
def home():
    return render_template("home.html")

# main content page for guests. book review listing
@app.route("/book_reviews", methods=["GET", "POST"])
def book_reviews():
    if request.method == "POST":
        query = request.form.get("search")
        books = list(mongo.db.books.find({"$text": {"$search": query}}))
        return render_template("books.html", books=books)
    books = mongo.db.books.find()
    return render_template("books.html", books=books)


# main content for users. user reviews listing
@app.route("/reviews")
def my_reviews():
    books = mongo.db.books.find()
    return render_template("my_reviews.html", books=books)    

# method for geting book info from database
def _extract_books(request):
    return {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "description": request.form.get("description"),
            "review": request.form.get("review"),
            "categories": request.form.get("categories"),
            "link": request.form.get("link"),
            "created_by": session["user"]
        }   

# Add review directory
@app.route("/review/add", methods=["GET", "POST"])
def make_review():
    if request.method == "POST":
        book = _extract_books(request)
        mongo.db.books.insert_one(book)
        flash("Book Review Successfully Added")
        return redirect(url_for("book_reviews"))

    return render_template("make_review.html")  

# Edit review directory
@app.route("/review/edit/<book_id>", methods=["GET", "POST"])
def edit_review(book_id):
    if request.method == "POST":
        edited = _extract_books(request)
        mongo.db.books.update({"_id": ObjectId(book_id)}, edited)
        flash("Book Review Successfully Updated")
        return redirect(url_for("my_reviews"))
    book = mongo.db.books.find_one({"_id": ObjectId(book_id)})
    return render_template("edit_review.html", book=book)

# delete review funtionality
@app.route("/review/delete/<book_id>")
def delete_review(book_id):
    mongo.db.books.remove({"_id": ObjectId(book_id)})
    flash("Review Successfully Deleted")
    return redirect(url_for("book_reviews"))

# register directory
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        # check if email already exists
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        if existing_email:
            flash("Email already has an account")
            return redirect(url_for("register"))
        # gets info from form
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "email": request.form.get("email").lower()
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("book_reviews"))
    return render_template("register.html")
    
# sign in directory
@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
    
        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("book_reviews"))
                
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("signin"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("signin"))

    return render_template("signin.html")


@app.route("/signout")
def signout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("book_reviews"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)