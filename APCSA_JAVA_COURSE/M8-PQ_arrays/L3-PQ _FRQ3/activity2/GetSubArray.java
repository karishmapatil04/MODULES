import java.util.Scanner;

public class GetSubArray {

    // Method to get a sub-array from the given array based on the start and end
    // indices
    public int[] getSubArray(int[] arr, int startIndex, int endIndex) {
        // Calculate the length of the sub-array
        int length = endIndex - startIndex + 1;

        // Initialize the result array to hold the sub-array
        int[] result = new int[length];

        // Copy the elements from the original array to the sub-array
        for (int i = startIndex; i <= endIndex; i++) {
            result[i - startIndex] = arr[i];
        }

        return result; // Return the sub-array
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources for automatic closing
            GetSubArray obj = new GetSubArray();

            // Ask the user to input the number of elements in the array
            System.out.print("Enter the number of elements in the array: ");
            int n = sc.nextInt();

            // Create an array to store the input elements
            int[] arr = new int[n];

            // Read the array elements from the user
            System.out.println("Enter the elements of the array:");
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            // Ask the user to input the start and end indices for the sub-array
            System.out.print("Enter the start index of the sub-array: ");
            int startIndex = sc.nextInt();
            System.out.print("Enter the end index of the sub-array: ");
            int endIndex = sc.nextInt();

            // Call the method to get the sub-array and store the result
            int[] subArray = obj.getSubArray(arr, startIndex, endIndex);

            // Display the sub-array
            System.out.print("Sub-array: ");
            for (int num : subArray) {
                System.out.print(num + " ");
            }
        }
    }
}