/*
__author__ = "Sabaini Chiara 3CI"
__version__  = "01.01"
__date__ = "2020-05-24"
*/

// link: https://studio.code.org/projects/applab/-8TJLrf_DoHsVbOx4ho0TZZeq67tAnnBEgd77kl1hUY

/*
    power

    Input: base, exponent
    Output: result of the power of base
*/
function power(base, exponent) {
    return Math.pow(base, exponent);
}

/*
    onEvent
    Handles button click, calling the power function
*/
onEvent("calculate", "click", function(base, exponent) {
    var base = parseInt(getText("base"));
    var exponent = parseInt(getText("exponent"));
    setText("result", power(base, exponent));
});
  