import java.util.Scanner;

public class ArrayReverse {

    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Prompt the user to input the number of elements (n) for the array
        System.out.print("Enter the number of elements in the array: ");
        int n = scn.nextInt();

        // Create an array of size n
        int[] arr = new int[n];

        // Prompt the user to input the elements of the array
        System.out.println("Enter the " + n + " elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt(); // Store each element in the array
        }

        // Call the method to display the array elements in reverse order
        displayArrReverse(arr, 0);
    }

    // Method to display array elements in reverse order
    public static void displayArrReverse(int[] arr, int idx) {
        // Base case: if index reaches the length of the array, return
        if (idx == arr.length) {
            return;
        }

        // Recursive call to display the next element
        displayArrReverse(arr, idx + 1);

        // Print the current element in reverse order after the recursive call
        System.out.println(arr[idx]);
    }
}