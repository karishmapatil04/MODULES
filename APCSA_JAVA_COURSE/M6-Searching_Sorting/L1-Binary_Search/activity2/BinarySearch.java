import java.util.Scanner;

class BinarySearch {
    // Recursive method to perform binary search
    // Returns index of x if it is present in arr[1..r], else return -1
    int binarySearch(int arr[], int l, int r, int x) {
        // Base case: If the range is valid
        if (r >= l) {
            int mid = l + (r - l) / 2;

            // If the element is present at mid
            if (arr[mid] == x)
                return mid;

            // If element is smaller than mid, it can only be present in the left subarray
            if (arr[mid] > x)
                return binarySearch(arr, l, mid - 1, x);

            // Else, the element can only be present in the right subarray
            return binarySearch(arr, mid + 1, r, x);
        }

        // Element is not present in the array
        return -1;
    }

    public static void main(String args[]) {
        // Create a scanner to get user input
        Scanner scn = new Scanner(System.in);

        // Prompt the user for input
        System.out.print("Enter the number of elements in the array: ");
        int n = scn.nextInt();

        // Create an array of size n
        int arr[] = new int[n];

        // Prompt the user to input elements in the sorted array
        System.out.println("Enter the elements of the array (sorted in ascending order): ");
        for (int i = 0; i < n; i++) {
            arr[i] = scn.nextInt();
        }

        // Prompt the user for the element to search
        System.out.print("Enter the element to search: ");
        int x = scn.nextInt();

        // Perform binary search on the array
        BinarySearch ob = new BinarySearch();
        int result = ob.binarySearch(arr, 0, n - 1, x);

        // Print the result of the search
        if (result == -1)
            System.out.println("Element is not present in the array");
        else
            System.out.println("Element is present at index " + result);
    }
}