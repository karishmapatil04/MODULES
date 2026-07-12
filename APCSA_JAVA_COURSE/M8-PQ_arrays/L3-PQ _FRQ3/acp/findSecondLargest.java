public static int findSecondLargest(int[] arr) {

    // Check if the array has fewer than two elements
    if (arr == null || arr.length < 2) {
        return -1;
    }

    int largest = Integer.MIN_VALUE;
    int secondLargest = Integer.MIN_VALUE;

    for (int num : arr) {
        if (num > largest) {
            secondLargest = largest;
            largest = num;
        } else if (num > secondLargest && num != largest) {
            secondLargest = num;
        }
    }

    // If no second largest element exists
    if (secondLargest == Integer.MIN_VALUE) {
        return -1;
    }

    return secondLargest;
}