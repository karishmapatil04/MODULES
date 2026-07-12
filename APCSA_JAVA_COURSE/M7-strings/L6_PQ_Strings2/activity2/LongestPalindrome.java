import java.util.Scanner;

public class LongestPalindrome {
    // Method to find the longest palindromic substring
    public String longestPalindrome(String str) {
        int n = str.length();
        boolean[][] isPalindrome = new boolean[n][n];

        // Every single character is a palindrome
        for (int i = 0; i < n; i++) {
            isPalindrome[i][i] = true;
        }

        // Check for two-character palindromes
        for (int i = 0; i < n - 1; i++) {
            if (str.charAt(i) == str.charAt(i + 1)) {
                isPalindrome[i][i + 1] = true;
            }
        }

        // Check for longer palindromes
        for (int len = 3; len <= n; len++) {
            for (int i = 0; i < n - len + 1; i++) {
                if (str.charAt(i) == str.charAt(i + len - 1) && isPalindrome[i + 1][i + len - 2]) {
                    isPalindrome[i][i + len - 1] = true;
                }
            }
        }

        // Find the longest palindrome
        int start = 0;
        int end = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                if (isPalindrome[i][j] && j - i > end - start) {
                    start = i;
                    end = j;
                }
            }
        }

        // Return the longest palindromic substring
        return str.substring(start, end + 1);
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources for automatic closing
            LongestPalindrome obj = new LongestPalindrome();

            // Prompt user for input
            System.out.print("Enter a string to find its longest palindromic substring: ");
            String input = sc.nextLine();

            // Call the method and display the result
            String result = obj.longestPalindrome(input);
            System.out.println("Longest Palindrome Substring: " + result);
        }
    }
}