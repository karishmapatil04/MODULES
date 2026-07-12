public class Main {

    // Kadane's Algorithm
    public static int kadane(int[] arr) {
        int maxSoFar = arr[0];
        int currentMax = arr[0];

        for (int i = 1; i < arr.length; i++) {
            currentMax = Math.max(arr[i], currentMax + arr[i]);
            maxSoFar = Math.max(maxSoFar, currentMax);
        }

        return maxSoFar;
    }

    // Concatenate the array k times
    public static int[] concatenate(int[] arr, int k) {
        int[] result = new int[arr.length * k];
        int index = 0;

        for (int i = 0; i < k; i++) {
            for (int num : arr) {
                result[index++] = num;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = { 1, -2, 3, 4, -1 };
        int k = 2;

        int[] concatArray = concatenate(arr, k);

        int maxSum = kadane(concatArray);

        System.out.println("Maximum Subarray Sum after " + k + "-time concatenation: " + maxSum);
    }
}
