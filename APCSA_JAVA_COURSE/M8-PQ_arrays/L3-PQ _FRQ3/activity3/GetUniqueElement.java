import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class GetUniqueElement {
    // Method to get unique elements from two arrays
    public int[] getUniqueElements(int[] arr1, int[] arr2) {
        Set<Integer> set = new HashSet<>();
        // Add elements from the first array to the set
        for (int num : arr1) {
            set.add(num);
        }
        // Add elements from the second array to the set
        for (int num : arr2) {
            set.add(num);
        }
        // Convert the set back to an array
        int[] result = new int[set.size()];
        int index = 0;
        // Fill the result array with unique elements from the set
        for (int num : set) {
            result[index] = num;
            index++;
        }
        return result; // Return the result array containing unique elements
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources to automatically close the scanner
            GetUniqueElement obj = new GetUniqueElement();
            // Read the size of the first array from the user
            System.out.print("Enter the size of the first array: ");
            int n1 = sc.nextInt();
            // Create the first array and read its elements
            int[] arr1 = new int[n1];
            System.out.println("Enter the elements of the first array:");
            for (int i = 0; i < n1; i++) {
                arr1[i] = sc.nextInt();
            }
            // Read the size of the second array from the user
            System.out.print("Enter the size of the second array: ");
            int n2 = sc.nextInt();
            // Create the second array and read its elements
            int[] arr2 = new int[n2];
            System.out.println("Enter the elements of the second array:");
            for (int i = 0; i < n2; i++) {
                arr2[i] = sc.nextInt();
            }
            // Call the method to get unique elements from both arrays
            int[] result = obj.getUniqueElements(arr1, arr2);
            // Display the result (unique elements from both arrays)
            System.out.print("Unique elements from both arrays: ");
            for (int num : result) {
                System.out.print(num + " ");
            }
        }
    }
}