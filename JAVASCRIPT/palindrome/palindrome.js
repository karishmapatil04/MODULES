function palindrome(myString) {
    // incase if any special characters or spaces are given in input that has to be removed.
    var input = myString.replace(/[^A-Z0-9]/ig, "").toLowerCase();

    var reversedInput = input.split('').reverse().join('');

    if (input === reversedInput) {
        document.write("<div>" + myString + " is a palindrome <div>")
    }
    else {
        document.write("<div>" + myString + " is not a palindrome <div>")
    }
}

palindrome("Race car")

