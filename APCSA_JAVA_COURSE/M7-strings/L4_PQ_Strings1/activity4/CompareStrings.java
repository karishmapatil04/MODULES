import java.util.Scanner;

public class CompareStrings {

    // Method to compare two strings lexicographically
    public int compareStrings(String str1, String str2) {
        // Loop through both strings character by character
        for (int i = 0; i < str1.length() && i < str2.length(); i++) {
            // Compare the characters at the current position
            if (str1.charAt(i) != str2.charAt(i)) {
                // Return the difference in the characters if they differ
                return str1.charAt(i) - str2.charAt(i);
            }
        }

        // If all characters are the same, compare the lengths
        return str1.length() - str2.length();
    }

    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner sc = new Scanner(System.in);
        CompareStrings obj = new CompareStrings();

        // Prompt the user to input two strings for comparison
        System.out.print("Enter the first string: ");
        String str1 = sc.nextLine();

        System.out.print("Enter the second string: ");
        String str2 = sc.nextLine();

        // Call the compareStrings method and print the result
        int result = obj.compareStrings(str1, str2);

        // Display the comparison result
        if (result == 0) {
            System.out.println("The strings are equal.");
        } else if (result < 0) {
            System.out.println("The first string is lexicographically smaller.");
        } else {
            System.out.println("The first string is lexicographically larger.");
        }
    }
}