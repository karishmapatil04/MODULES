import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class LongestConsecutiveSequence {

    // Method to find the length of the longest consecutive sequence in the array
    public int findLongestConsecutiveSequence(int[] arr) {
        Set<Integer> set = new HashSet<>();
        // Add all elements to the set to allow O(1) lookups
        for (int num : arr) {
            set.add(num);
        }
        int maxLength = 0;
        // Loop through each element in the array
        for (int num : arr) {
            // Only start checking if the current number is the start of a sequence
            int length = 1;
            // If the previous number is not in the set, we know this is the start of a
            // sequence
            if (!set.contains(num - 1)) {
                int currentNum = num;
                // Check the next consecutive numbers
                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    length++;
                }
                // Update the maximum length found so far
                maxLength = Math.max(maxLength, length);
            }
        }
        return maxLength;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources for automatic closing
            LongestConsecutiveSequence obj = new LongestConsecutiveSequence();
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
            // Call the method and display the result
            int result = obj.findLongestConsecutiveSequence(arr);
            System.out.println("The length of the longest consecutive sequence is: " + result);
        }
    }
}