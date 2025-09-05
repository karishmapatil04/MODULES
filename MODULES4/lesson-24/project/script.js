function percentage() {

    // Method returns the element of percent id
    let percent = document.getElementById("percent").value;

    // Method returns the element of num id
    let num = document.getElementById("num").value;
    document.getElementById("value1")
        .value = (num / 100) * percent;
}
