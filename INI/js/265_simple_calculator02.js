/*
__author__ = "Sabaini Chiara 3CI"
__version__  = "01.01"
__date__ = "2020-05-25"
*/

// link: https://studio.code.org/projects/applab/KjGjtUFAcRT8PiZR4SD52TdhLeG941OQbLDmbEqrA7I


var operation = "";

onEvent("00", "click", function( ){
    operation = operation+"00";
    setText("operation", operation);
});

onEvent("0", "click", function( ){
    operation = operation+"0";
    setText("operation", operation);
});

onEvent("1", "click", function( ){
    operation = operation+"1";
    setText("operation", operation);
});

onEvent("2", "click", function( ){
    operation = operation+"2";
    setText("operation", operation);
});

onEvent("3", "click", function( ){
    operation = operation+"3";
    setText("operation", operation);
});

onEvent("4", "click", function( ){
    operation = operation+"4";
    setText("operation", operation);
});

onEvent("5", "click", function( ){
    operation = operation+"5";
    setText("operation", operation);
});

onEvent("6", "click", function( ){
    operation = operation+"6";
    setText("operation", operation);
});

onEvent("7", "click", function( ){
    operation = operation+"7";
    setText("operation", operation);
});

onEvent("8", "click", function( ){
    operation = operation+"8";
    setText("operation", operation);
});

onEvent("9", "click", function( ){
    operation = operation+"9";
    setText("operation", operation);
});

onEvent("+", "click", function( ){
    operation = operation+"+";
    setText("operation", operation);
});

onEvent("-", "click", function( ){
    operation = operation+"-";
    setText("operation", operation);
});

onEvent("*", "click", function( ){
    operation = operation+"*";
    setText("operation", operation);
});

onEvent("/", "click", function( ){
    operation = operation+"/";
    setText("operation", operation);
});

onEvent("DEL", "click", function( ){
    operation = operation.substring(0, operation.length - 1);
    setText("operation", operation);
});

onEvent("C", "click", function( ){
    operation = "";
    setText("operation", operation);
});

/*
    onEvent
    Handles button click, changing label's text
    with the result of the operation given by the user
*/
onEvent("=", "click", function(){
    operation = eval(operation).toString();
    setText("operation", operation);
});