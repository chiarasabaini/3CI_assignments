/*
__author__ = "Sabaini Chiara 3CI"
__version__  = "01.01"
__date__ = "2020-05-25"
*/

// link: https://studio.code.org/projects/applab/R4It9z7MzDXysErNaZ9IxwBwHSlrNaPLn06IG35nkUg

var x = 110;
var y = 70;
var step = 3;
var dir = "";

/*
    control
    gets the coordinates of the img,
    controls if they reach the limits of screen  
*/
function control(){
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
    move_flappy
    changes the coordinates of the img

    Input: dir - direction
*/
function move_flappy(dir){
    if (dir == "up"){
        y -= step;
    }
    if (dir == "down"){
        y += step;
    }
    if (dir == "right"){
        x += step;
    }
    if (dir == "left"){
        x -= step;
    }
}

/*
    onEvent
    Handles button click, changing direction
*/
onEvent("right", "click", function( ) {
    dir = "right";
});
  
onEvent("left", "click", function( ) {
    dir = "left";
});
  
onEvent("up", "click", function( ) {
    dir = "up";
});
  
onEvent("down", "click", function( ) {
    dir = "down";
});

/*
    timedLoop
    it's a timed loop that makes the img move
    continuously
*/
timedLoop(33, function () {
    control();
    move_flappy(dir);
    setPosition("flappy_bird", x, y);
});