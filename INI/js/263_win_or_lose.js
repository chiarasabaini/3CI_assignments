/*
__author__ = "Sabaini Chiara 3CI"
__version__  = "01.01"
__date__ = "2020-05-24"
*/

// link: https://studio.code.org/projects/applab/wpMjE9YbMODjqFoEg1m0c-I8BJxSJkSVMhM71cYG-4Q

/*
    onEvent
    Handles button click, changing label's text based
    on a random value
*/
onEvent("try", "click", function() {
    // determinating if it's time to lose or to win
    var result = randomNumber(0, 1);

    if (result == 1){
        result = "YOU WON!! :)";
    } else {
        result = "OH NO, YOU LOST!!\nTRY AGAIN!";
    }
    // setting the label's text
    setText("result", result);
});
