import java.util.Arrays;

public static double findMedian(int[] arr) {

    // Sort the array
    Arrays.sort(arr);

    int n = arr.length;

    // If the array length is odd
    if (n % 2 != 0) {
        return arr[n / 2];
    }

    // If the array length is even
    return (arr[n / 2 - 1] + arr[n / 2]) / 2.0;
}