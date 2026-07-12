import java.util.Scanner;

public class SelectionSort {

    // Method to perform selection sort on the array
    void sort(int arr[]) {
        int n = arr.length;

        // One by one move the boundary of the unsorted subarray
        for (int i = 0; i < n - 1; i++) {
            // Find the minimum element in the unsorted array
            int min_idx = i;
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[min_idx])
                    min_idx = j;
            }

            // Swap the found minimum element with the first element
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }

    // Method to print the array
    void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; i++)
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
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt(); // Read each element
        }

        // Create an instance of SelectionSort
        SelectionSort ob = new SelectionSort();

        // Call the sort method to sort the array
        ob.sort(arr);

        // Print the sorted array
        System.out.println("Sorted array:");
        ob.printArray(arr);
    }
}