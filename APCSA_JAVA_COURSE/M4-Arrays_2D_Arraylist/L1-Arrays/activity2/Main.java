import java.util.Scanner;

public class FindElementArray {

    // Main method - Entry point of the program
    public static void main(String[] args) {

        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Prompt the user to enter the element to search for (d)
        System.out.print("Enter the element to search for: ");
        int d = scn.nextInt();

        // Prompt the user to enter the size of the array (n)
        System.out.print("Enter the number of elements in the array: ");
        int n = scn.nextInt();

        // Create an integer array to store the elements
        int[] arr = new int[n];

        // Prompt the user to enter the elements of the array
        System.out.println("Enter the " + n + " elements of the array:");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt(); // Store each input value in the array
        }

        // Call the find method to find the index of the element in the array
        int ans = find(arr, d);

        // Print the result (index of the element or -1 if not found)
        System.out.println(ans);
    }

    // Method to find the index of an element in the array
    // Returns the index if found, otherwise returns -1
    public static int find(int[] arr, int d) {

        // Loop through the array to check for the element
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == d) { // If the element is found
                return i; // Return the index of the element
            }
        }

        // If the element is not found, return -1
        return -1;
    }
}
