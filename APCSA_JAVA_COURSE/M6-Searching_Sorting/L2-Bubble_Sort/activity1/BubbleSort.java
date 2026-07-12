import java.util.Scanner;

class BubbleSort {
    // An optimized version of Bubble Sort
    static void bubbleSort(int arr[], int n) {
        int i, j, temp;
        boolean swapped;

        // Outer loop to traverse through all elements
        for (i = 0; i < n - 1; i++) {
            swapped = false;

            // Inner loop to compare adjacent elements
            for (j = 0; j < n - i - 1; j++) {
                // If the current element is greater than the next element, swap them
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j + 1]
                    temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }

            // If no elements were swapped, the array is already sorted, break out of the
            // loop
            if (!swapped)
                break;
        }
    }

    // Function to print the array
    static void printArray(int arr[], int size) {
        for (int i = 0; i < size; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }

    public static void main(String args[]) {
        // Create a scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Prompt user for the number of elements in the array
        System.out.print("Enter the number of elements: ");
        int n = scn.nextInt();

        // Create an array to store elements
        int[] arr = new int[n];

        // Prompt the user to input the elements of the array
        System.out.println("Enter the elements:");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt(); // Read each element
        }

        // Call the bubbleSort method to sort the array
        bubbleSort(arr, n);

        // Display the sorted array
        System.out.println("Sorted array: ");
        printArray(arr, n);
    }
}