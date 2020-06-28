/*
__author__ = "Sabaini Chiara 3CI"
__version__  = "01.01"
__date__ = "2020-05-25"
*/

// link: https://studio.code.org/projects/applab/dwDxk7Uf1uCsw4OohJNA2ClNVYIsEsKi7pN5Hz2RhPM

var x = 110;
var y = 70;
var step = 10;

/*
    control
    gets the coordinates of the img,
    controls if they reach the limits of screen  
*/
function control(){
    x = getProperty("flappy_bird", "x");
    y = getProperty("flappy_bird", "y");
    if (x > 320){
        x = 0;
    }
    if (x < 0){
        x = 310;
    }
    if (y > 180){
        y = 0;
    }
    if (y < 0){
        y = 180;
    }
}

/*
    onEvent
    Handles button click, changing img's position
    by step value
*/
onEvent("right", "click", function( ) {
    control();
    setPosition("flappy_bird", x + step, y);
});

onEvent("left", "click", function( ) {
    control();
    setPosition("flappy_bird", x - step, y);
});

onEvent("up", "click", function( ) {
    control();
    setPosition("flappy_bird", x, y - step);
});

onEvent("down", "click", function( ) {
    control();
    setPosition("flappy_bird", x, y + step);
});