import java.util.Scanner;

public class InsertionSort {

    // Function to sort array using insertion sort
    void sort(int arr[]) {
        int n = arr.length;

        // Traverse through i to n
        for (int i = 1; i < n; ++i) {
            int key = arr[i]; // The element to be inserted
            int j = i - 1;

            // Move elements of arr[0..i-1], that are greater than key,
            // to one position ahead of their current position
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j = j - 1;
            }
            arr[j + 1] = key; // Insert the key at its correct position
        }
    }

    // A utility function to print the array of size n
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Prompt the user to input the number of elements in the array
        System.out.print("Enter the number of elements: ");
        int n = scn.nextInt();

        // Create an array of size n
        int arr[] = new int[n];

        // Prompt the user to input the elements of the array
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; ++i) {
            arr[i] = scn.nextInt(); // Read each element
        }

        // Create an instance of InsertionSort
        InsertionSort ob = new InsertionSort();

        // Call the sort method to sort the array
        ob.sort(arr);

        // Print the sorted array
        System.out.println("Sorted array:");
        printArray(arr);
    }
}