import java.util.Scanner;

public class IsSorted {

    // Method to check if the array is sorted in ascending order
    public boolean isSorted(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            // If any element is smaller than the previous element, return false
            if (arr[i] < arr[i - 1]) {
                return false;
            }
        }

        return true; // If no such element is found, the array is sorted
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources for automatic closing
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

            // Create an object of IsSorted and call the isSorted method
            IsSorted obj = new IsSorted();
            boolean result = obj.isSorted(arr);

            // Print whether the array is sorted or not
            if (result) {
                System.out.println("The array is sorted.");
            } else {
                System.out.println("The array is not sorted.");
            }
        }
    }
}