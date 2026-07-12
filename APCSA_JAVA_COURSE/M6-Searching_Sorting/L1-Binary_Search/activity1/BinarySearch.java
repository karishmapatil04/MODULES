import java.util.Scanner;

class BinarySearch {
    // Returns index of x if it is present in arr[].
    int binarySearch(int arr[], int x) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;

            // Check if x is present at mid
            if (arr[m] == x)
                return m;

            // If x is greater, ignore left half
            if (arr[m] < x)
                l = m + 1;

            // If x is smaller, ignore right half
            else
                r = m - 1;
        }

        // If we reach here, then element was not present
        return -1;
    }

    public static void main(String args[]) {
        Scanner scn = new Scanner(System.in);

        // Prompt the user to enter the size of the array
        System.out.print("Enter the number of elements in the array: ");
        int n = scn.nextInt();

        // Create an array and prompt the user to input its elements
        int arr[] = new int[n];
        System.out.println("Enter the elements of the array (sorted in ascending order):");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt();
        }

        // Prompt the user to input the element to be searched
        System.out.print("Enter the element to search: ");
        int x = scn.nextInt();

        BinarySearch ob = new BinarySearch();
        int result = ob.binarySearch(arr, x);

        // Output the result of the search
        if (result == -1)
            System.out.println("Element is not present in the array");
        else
            System.out.println("Element is present at index " + result);
    }
}