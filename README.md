![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# MEETPORTUGAL website
[View the live project!](https://mymilestoneproject.herokuapp.com/)

This website was created for my third milestone project and its goal is to provide an easy and elegant way of finding and recommending books!
## User Experience (UX)
 ### User Stories
     
     1.1- As a user  
        1.1.1- I need to navigate easily and fluidly through the website;
        1.1.2- I want to easily recognise what the website is about;
        1.1.3- I must be able to easily register while geting warnings if there is any errors;
        1.1.4- I must be able to sign in and out without problems with warnings in case any errors are made;
        1.1.5- I require an easy way to find reviews of a particular book or author;
        1.1.6- I must be able to make my own reviews;
        1.1.7- I must be able to edit my own reviews in case i need to make changes;
        1.1.8- I need to be able to delete reviews;
        1.1.9- I need to be able to find contact information of the website owner in case I wannt to reach him/her;
    
2.1-Homepage Wireframe
[Home Desktop Wireframe](static/img/home.png)
[Home Mobile Wireframe](static/img/home_mobile.png)  

2.2-Books page Wireframe
[Books Desktop Wireframe](static/img/books.png)
[Books Mobile Wireframe](static/img/books_mobile.png)

2.3-My Reviews page Wireframe
[My Reviews Desktop Wireframe](static/img/my_reviews.png)
[My Reviews Mobile Wireframe](static/img/my_reviews_mobile.png)

2.4-Sign in page Wireframe
[Sign in Desktop Wireframe](static/img/sign_in.png)
[Sign in Mobile Wireframe](static/img/sign_in_mobile.png)

2.5-Register page Wireframe
[Register Desktop Wireframe](static/img/register.png)
[Register Mobile Wireframe](static/img/register_mobile.png) 

2.6-Make Review page Wireframe
[Make Review Desktop Wireframe](static/img/make_review.png)
[Make Review Mobile Wireframe](static/img/make_review_mobile.png) 

2.6-Edit Review page Wireframe
[Edit Review Desktop Wireframe](static/img/edit_review.png)
[Edit Review Mobile Wireframe](static/img/edit_review_mobile.png) 

### Design

    3.1- Color Scheme
    The two colors used are black and white with amber in the book review links.

    3.2- Typography
    In this website the titles are written in Tangering while all the other text is default. 

    3.3- Images
    Two images are included in the website to give context and information to the website. Fist one being the home page background image and then for each review there is a default image.

## Features

    4.1- Website designed to be responsive on all sizes;
    4.2- Website uses Materialize to provide Css making the looks more appealing and functional.
    4.3- All CRUD (Create, Read, Update, Delete) are working together with a search funtionality that is key to any book review website.

## Technologies Used

### Languages Used

    5.1- HTML5;
   
    5.2- CSS3;

    5.3- Javascript

    5.4- Python3

### Frameworks, Libraries and Programs Used

    6.1- Bootstrap 4.4.1:
    Used to style and make website responsive;

    6.2- Javascript:
    Used to initialize some components;

    6.3- Google Fonts:
    Used to import Tangerine;

    6.4- jQuery:
    Used to make navigation bar responsive and make the dropdown button work together with some materialize options;

    6.5- GitHub:
    Used to store and manage the project;

    6.6- Balsamiq:
    Used to create my Wireframes;

    6.7-Flask:
    Used to work with databases;

    6.8-Mongodb:
    Used to create and store databases;

## Testing

The website's code passed both W3C HTML5 test and CSS3 test.

### Testing User Stories

1.1.1- As a user I need to navigate easily and fluidly through the website:

    All Navigator links work perfectly and are responsive. Turns into dropdown menu when it is supose to;
    
    Test #: 1
    Action Taken: Click on "Bookers" in Nav bar
    ﻿"Before" State: No hoover or change.
    ﻿"After" State: home.html was loaded when pressing logo on whatever page we are located.
    ﻿Test Result: Successful
    
    Test #: 2
    Action Taken: Click on "Book Reviews" in Nav bar
    ﻿"Before" State: Book Reviews link had gold color while hoovered on all pages.
    ﻿"After" State: books.html was loaded when pressing Book Reviews link on whatever page we are located.
    ﻿Test Result: Successful

    Test #: 3
    Action Taken: Click on "My Reviews" in Nav bar
    ﻿"Before" State: My Reviews link had gold color while hoovered on all pages.
    ﻿"After" State: my_reviews.html was loaded when pressing it's link on whatever page we are located.
    ﻿Test Result: Successful

    Test #: 4
    Action Taken: Click on "New Review" in Nav bar
    ﻿"Before" State: New Review link had gold color while hoovered on all pages.
    ﻿"After" State: make_review.html was loaded when pressing it's link on whatever page.
    ﻿Test Result: Successful

    Test #: 5
    Action Taken: Click on "Sign Out" in Nav bar
    ﻿"Before" State: Sign out link had gold color while hoovered on all pages.
    ﻿"After" State: User Signed out on whatever page we are located.
    ﻿Test Result: Successful

    Test #: 6
    Action Taken: Click on "Sign In" in Nav bar
    ﻿"Before" State: Sign In link had gold color while hoovered on all pages.
    ﻿"After" State: signin.html was loaded when pressing it's link on whatever page.
    ﻿Test Result: Successful

    Test #: 7
    Action Taken: Click on "Register" in Nav bar
    ﻿"Before" State: Register link had gold color while hoovered on all pages.
    ﻿"After" State: register.html was loaded when pressing it's link on whatever page.
    ﻿Test Result: Successful

   


1.1.2- As a user I want to easily recognise what the website is about:

    Home page clealy explains what the purpose of the website is.
    
    Test #: 1
    Action Taken: Tried finding a book review for harry potter.
    ﻿"Before" State:All book reviews were shown.
    ﻿"After" State:Found all harry potter related books in database.
    ﻿Test Result: Successful
    

 1.1.3- I must be able to easily register while geting warnings if there is any errors:

    Register is working as intended and in case of error it gives a warning massage.

    Test #: 1
    Action Taken: Tried already used username
    ﻿"Before" State: Empty box ready for user input
    ﻿"After" State: "username alredy in use" message received
    ﻿Test Result: Successful

    Test #: 2
    Action Taken: Tried already used email
    ﻿"Before" State: Empty box ready for user input
    ﻿"After" State: "Email already has an account" message received
    ﻿Test Result: Successful

    Test #: 3
    Action Taken: Tried submiting with empty fields
    ﻿"Before" State: Empty box ready for user input on one of the fields
    ﻿"After" State: "Please fill out this field" message received on whatever field is blank.
    ﻿Test Result: Successful
  

1.1.4- I must be able to sign in and out without problems with warnings in case any errors are made:

   Sign out funtionality already tested in usercase 1.1.1 and testings found that sign in is working as intended
     Test #: 1
    Action Taken: Tried unregistered username
    ﻿"Before" State: Empty box ready for user input
    ﻿"After" State: "Incorrect Username and/or Password" message received
    ﻿Test Result: Successful

    Test #: 2
    Action Taken: Tried wrong password
    ﻿"Before" State: Empty box ready for user input
    ﻿"After" State: "Incorrect Username and/or Password" message received
    ﻿Test Result: Successful

    Test #: 3
    Action Taken: Tried submiting with empty fields
    ﻿"Before" State: Empty box ready for user input on one of the fields
    ﻿"After" State: "Please fill out this field" message received on whatever field is blank.
    ﻿Test Result: Successful


1.1.5- I require an easy way to find reviews of a particular book or author:

    Search funtionality tested on previous testings.
    Test #: 1
    Action Taken:  Checked if no results were found page would crash.
    ﻿"Before" State: Input "corki" on search area
    ﻿"After" State: No reviews shown but page works as intended
    ﻿Test Result: Successful

    Future funtionalities: Add No results were found text!

1.1.6- I must be able to make my own reviews:    
    Page opens as intended.
     Test #: 1
    Action Taken: Tried submiting with empty fields
    ﻿"Before" State: Empty box ready for user input on one of the fields
    ﻿"After" State: "Please fill out this field" message received on whatever field is blank.
    ﻿Test Result: Successful

     Test #: 2
    Action Taken: Tried submiting as intended
    ﻿"Before" State: Filled up inputs on one of the fields
    ﻿"After" State: Redirected to my reviews page with added review
    ﻿Test Result: Successful

1.1.7- I must be able to edit my own reviews in case i need to make changes:

    Page opens as intended.
     Test #: 1
    Action Taken: Tried submiting with empty fields
    ﻿"Before" State: Empty box ready for user input on one of the fields
    ﻿"After" State: "Please fill out this field" message received on whatever field is blank.
    ﻿Test Result: Successful

     Test #: 2
    Action Taken: Tried submiting as intended
    ﻿"Before" State: changed some of the text on one of the fields and clicked edit.
    ﻿"After" State: Redirected to my reviews page with the eddited review.
    ﻿Test Result: Successful

1.1.8- I need to be able to delete reviews:
    
    
     Test #: 1
    Action Taken: Tried deleting a review
    ﻿"Before" State: Review showing on my review page
    ﻿"After" State: "Review successfully deleted" message and my review page opens without deleted review.
    ﻿Test Result: Successful

1.1.9- I need to be able to find contact information of the website owner in case I wannt to reach him/her:

    Footer working on all pages except home page as intended.

## Further Testing

    Website was tested on Firefox and Chrome on all diferent sizes from mobile to desktop.
    Friends and family tested and critiqued website which helped with some last few design details.


## Known Bugs

   Sometimes when checking website on mobile the borders show but after changing the page the no longer appear.



## Credits

### Code 

Website was made based on the walkthrough project provided by code institute on task manager.


### Content 

    All content was written by the developer sometimes based on task manager walkthrough project.

### Media

    All images are from the google images.

## Deployment 

### Github Pages 
The project was deployed to GitHub Pages using the following steps:

    1-Log in to GitHub and locate the GitHub Repository;

    2-At the top of the Repository, press "Settings" Button;

    3-Scroll down the Settings until the "GitHub Pages" Section.

    4-Under "Source", click the dropdown and select "Master Branch".

    5-After the page refreshes scroll back into the previous section and find the published site link.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account so that we can modify it without being worried about changing the orinal repository.

    1-To do this log in to GitHub and locate the GitHub Repository;

    2-At the top of the Repository just above the "Settings" Button press the "Fork" Button;

    3-You will now have a forked vertion of the original repository in your GitHub account;

### Making a Local Clone

    1-Log in to GitHub and locate the GitHub Repository;

    2-Under the repository name, click "Clone or download";

    3-To clone the repository using HTTPS, under "Clone with HTTPS", copy the link;

    4-Open Git Bash;

    5-Change the current working directory to the location where you want the cloned directory to be made;

    6-Type git clone, and then paste the URL you copied previously;

    7-$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

    8-Press Enter. Your local clone will be created.

## Acknoledgements

My Mentor for guiding me and making sure I dont skip important steps. Special thanks to code institute online tutors that helped me make google maps API work and tried to help me integrate a different Hotel api(even if it did not work).