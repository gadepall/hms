$(function() {
	
//$(document).ready(function () {
$(".alphaonly").on("keypress", function(event) {
	
    // Disallow anything not matching the regex pattern (A to Z uppercase, a to z lowercase and white space)
    // For more on JavaScript Regular Expressions, look here: https://developer.mozilla.org/en-US/docs/JavaScript/Guide/Regular_Expressions
    var englishAlphabetAndWhiteSpace = /[A-Za-z ]/g;

    // Retrieving the key from the char code passed in event.which
    // For more info on even.which, look here: http://stackoverflow.com/q/3050984/114029
    var key = String.fromCharCode(event.which);

    //alert(event.keyCode);

    // For the keyCodes, look here: http://stackoverflow.com/a/3781360/114029
    // keyCode == 8  is backspace
    // keyCode == 37 is left arrow
    // keyCode == 39 is right arrow
    // englishAlphabetAndWhiteSpace.test(key) does the matching, that is, test the key just typed against the regex pattern
    if (event.keyCode == 8 || englishAlphabetAndWhiteSpace.test(key)) {
        return true;
    }

    // If we got this far, just return false because a disallowed key was typed.
    return false;
});
});
$('.alphaonly').on("paste",function(e)
{
    e.preventDefault();
});



$(function() {
	
//$(document).ready(function () {
$(".spalphanum").on("keypress", function(event) {
 
   

   
    //var key = String.fromCharCode(event.which);
    if(event.keyCode == 34 || event.keyCode == 39) {
		 //display error message
        $("#errmsg").html("alpanum Only").show().fadeOut("slow");
              
        return false;
    }
});
});

$('.spalphanum').on("paste",function(e)
{
    e.preventDefault();
});




$(function() {

  //called when key is pressed in textbox
  $(".numeric").keypress(function (e) {

     //if the letter is not digit then display error and don't type anything
     if (e.which != 8 && e.which != 0 && (e.which < 46 || e.which > 57)) {
        //display error message
        $("#err").html("Digits Only").show().fadeOut("slow");
               return false;
    }
   });
});


$(function() {
	
//$(document).ready(function () {
$(".alphanumeric").on("keypress", function(event) {
	
    var englishAlphaNumericAndWhiteSpace = /[0-9A-Za-z ]/g;

   
    var key = String.fromCharCode(event.which);

   
    if (event.keyCode == 8 || englishAlphaNumericAndWhiteSpace.test(key) || event.keyCode ==46) {
        return true;
    }

    // If we got this far, just return false because a disallowed key was typed.
    return false;
});
});
$('.alphanumeric').on("paste",function(e)
{
    e.preventDefault();
});


