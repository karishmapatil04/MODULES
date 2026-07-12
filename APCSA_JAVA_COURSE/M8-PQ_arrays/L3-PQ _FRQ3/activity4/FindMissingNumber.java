import java.util.Scanner;
import java.util.HashSet;

public class FindMissingNumber {
    // Method to find the missing number in the array
    public int findMissingNumber(int[] arr, int n) { // Added n parameter
        // Using HashSet to track numbers
        HashSet<Integer> numbers = new HashSet<>();

        // Add all array elements to set
        for (int num : arr) {
            numbers.add(num);
        }

        // Check numbers from 1 to n+1
        for (int i = 1; i <= n + 1; i++) {
            if (!numbers.contains(i)) {
                return i;
            }
        }

        return -1; // Error case
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            FindMissingNumber obj = new FindMissingNumber();

            System.out.print("Enter the size of the array (excluding the missing number): ");
            int n = sc.nextInt();

            if (n <= 0) {
                System.out.println("Array size must be positive");
                return;
            }

            int[] arr = new int[n];
            System.out.println("Enter " + n + " different numbers between 1 and " + (n + 1) + ":");

            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            int missingNumber = obj.findMissingNumber(arr, n);
            if (missingNumber != -1) {
                System.out.println("The missing number is: " + missingNumber);
            } else {
                System.out.println("No missing number found");
            }
        }
    }
}