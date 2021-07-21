$(document).ready(function(){
    $('.sidenav').sidenav();
  });

$("#nav_title").mouseenter(function () {
    $(this).addClass("color-gold");
});
$("#nav_title").mouseleave(function () {
    $(this).removeClass("color-gold");
});