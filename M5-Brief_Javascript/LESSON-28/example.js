try {
    var userInput = prompt("Please type a number to divide 100 by:");
    var n = Number(userInput);
    if (isNaN(n)) { throw "Please type a valid number!"; }
    console.log(100 / n);
} catch (err) {
    console.log("Error: " + err);
}