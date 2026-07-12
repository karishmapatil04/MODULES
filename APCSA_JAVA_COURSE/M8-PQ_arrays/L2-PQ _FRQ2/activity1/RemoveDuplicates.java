import java.util.Scanner;

public class RemoveDuplicates {
    // Method to remove duplicate elements from an array
    public int[] removeDuplicates(int[] arr) {
        int[] result = new int[arr.length];
        int index = 0;

        // Loop through each element of the array
        for (int i = 0; i < arr.length; i++) {
            boolean duplicate = false;

            // Check if the element is already in the result array
            for (int j = 0; j < index; j++) {
                if (arr[i] == result[j]) {
                    duplicate = true;
                    break;
                }
            }

            // If no duplicate, add it to the result array
            if (!duplicate) {
                result[index] = arr[i];
                index++;
            }
        }

        // Trim the result array to remove extra space
        int[] trimmedResult = new int[index];
        for (int i = 0; i < index; i++) {
            trimmedResult[i] = result[i];
        }

        return trimmedResult;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources
            // Ask the user to input the number of elements in the array
            System.out.print("Enter the number of elements: ");
            int n = sc.nextInt();

            // Create an array to store the input elements
            int[] arr = new int[n];

            // Read the array elements from the user
            System.out.println("Enter the elements:");
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            // Create an object of RemoveDuplicates and call the removeDuplicates method
            RemoveDuplicates obj = new RemoveDuplicates();
            int[] result = obj.removeDuplicates(arr);

            // Print the array after removing duplicates
            System.out.println("Array after removing duplicates:");
            for (int value : result) {
                System.out.print(value + " ");
            }
        }
    }
}