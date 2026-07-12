public class Main {

    // Recursive method to find the maximum element
    public static int findMax(int[] arr, int index) {
        // Base case
        if (index == arr.length - 1) {
            return arr[index];
        }

        // Recursive call
        int max = findMax(arr, index + 1);

        // Return the larger value
        return Math.max(arr[index], max);
    }

    public static void main(String[] args) {
        int[] arr = { 12, 45, 7, 89, 34, 56 };

        int maxElement = findMax(arr, 0);

        System.out.println("Maximum Element: " + maxElement);
    }
}