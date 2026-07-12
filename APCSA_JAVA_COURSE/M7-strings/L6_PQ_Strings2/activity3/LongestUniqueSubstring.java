import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class LongestUniqueSubstring {
    // Method to find the longest unique substring
    public String longestUniqueSubstring(String str) {
        Set<Character> seen = new HashSet<>();
        int start = 0;
        String longest = "";

        // Loop through the string
        for (int i = 0; i < str.length(); i++) {
            // If the character is already in the set, remove the start character and move
            // start forward
            while (seen.contains(str.charAt(i))) {
                seen.remove(str.charAt(start));
                start++;
            }
            // Add the current character to the set
            seen.add(str.charAt(i));

            // Update the longest unique substring
            if (i - start + 1 > longest.length()) {
                longest = str.substring(start, i + 1);
            }
        }

        return longest;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        LongestUniqueSubstring obj = new LongestUniqueSubstring();

        // Ask for user input
        System.out.print("Enter a string to find its longest unique substring: ");
        String input = scanner.nextLine();

        // Get and print the result
        String result = obj.longestUniqueSubstring(input);
        System.out.println("Longest unique substring: " + result);
    }
}