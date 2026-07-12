import java.util.Scanner;

public class DisplayArray {

    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Ask the user for the number of elements in the array
        System.out.print("Enter the number of elements in the array: ");
        int n = scn.nextInt();

        // Create an integer array of size n
        int[] arr = new int[n];

        // Ask the user to input the elements of the array
        System.out.println("Enter the " + n + " elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt(); // Store each element in the array
        }

        // Call the method to display the array elements starting from index 0
        displayArr(arr, 0);
    }

    // Method to display array elements recursively
    public static void displayArr(int[] arr, int idx) {
        // Base case: if index reaches the length of the array, return
        if (idx == arr.length) {
            return;
        }

        // Print the current element of the array
        System.out.println(arr[idx]);

        // Recursive call to display the next element
        displayArr(arr, idx + 1);
    }
}