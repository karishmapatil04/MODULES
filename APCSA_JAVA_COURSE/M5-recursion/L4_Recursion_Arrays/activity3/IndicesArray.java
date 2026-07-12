import java.util.Scanner;

public class IndicesArray {

    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Prompt the user to input the number of elements (n) in the array
        System.out.print("Enter the number of elements in the array: ");
        int n = scn.nextInt();

        // Create an array to store the integers
        int[] arr = new int[n];

        // Prompt the user to input the elements of the array
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt(); // Store each element in the array
        }

        // Ask the user for the number to find the indices of
        System.out.print("Enter the number to find indices: ");
        int x = scn.nextInt();

        // Call the method to find and print all indices of the number x in the array
        AllIndexes(arr, n, x);
    }

    // Recursive method to find all indices of a number in the array
    public static int AllIndexesRecursive(int[] input, int size, int x, int[] output) {
        // Base case: If the input array becomes empty
        if (size == 0)
            return 0;

        // Get the recursive answer by calling the function on the remaining part of the
        // array
        int smallAns = AllIndexesRecursive(input, size - 1, x, output);

        // If the last element of the input array is equal to x
        if (input[size - 1] == x) {
            // Insert the index of the last element into the output array and increment
            // smallAns
            output[smallAns++] = size - 1;
        }
        return smallAns; // Return the total count of indices found
    }

    // Function to find all indices of a number in the input array
    static void AllIndexes(int[] input, int n, int x) {
        // Create an output array to store the indices
        int[] output = new int[n];

        // Call the recursive method to get the indices
        int size = AllIndexesRecursive(input, n, x, output);

        // Print all indices stored in the output array
        for (int i = 0; i < size; i++) {
            System.out.print(output[i] + " "); // Print each index
        }
    }
}