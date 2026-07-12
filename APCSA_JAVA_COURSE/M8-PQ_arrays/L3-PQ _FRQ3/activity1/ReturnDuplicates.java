import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class ReturnDuplicates {
    // Method to find and return duplicate elements in the array
    public int[] findDuplicates(int[] arr) {
        Set<Integer> uniqueValues = new HashSet<>();
        Set<Integer> duplicateValues = new HashSet<>();

        // Loop through the array to check for duplicates
        for (int num : arr) {
            if (!uniqueValues.add(num)) { // If adding to the set fails, it means the number is a duplicate
                duplicateValues.add(num); // Add the duplicate number to the duplicate set
            }
        }

        // Convert the duplicate values set to an array
        int[] result = new int[duplicateValues.size()];
        int index = 0;

        // Transfer the elements from the duplicate set to the result array
        for (int num : duplicateValues) {
            result[index] = num;
            index++;
        }

        return result; // Return the array containing the duplicates
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources for automatic closing
            ReturnDuplicates obj = new ReturnDuplicates();

            // Ask the user to input the number of elements in the array
            System.out.print("Enter the number of elements: ");
            int n = sc.nextInt();

            // Create an array to store the input elements
            int[] arr = new int[n];

            // Read the array elements from the user
            System.out.println("Enter the elements:");
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            // Call the method to find duplicates and store the result
            int[] result = obj.findDuplicates(arr);

            // Display the duplicates found
            if (result.length > 0) {
                System.out.print("Duplicates found: ");
                for (int num : result) {
                    System.out.print(num + " ");
                }
            } else {
                System.out.println("No duplicates found.");
            }
        }
    }
}