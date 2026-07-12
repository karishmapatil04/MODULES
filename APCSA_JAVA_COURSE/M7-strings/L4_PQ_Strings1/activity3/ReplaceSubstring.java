import java.util.Scanner;

public class ReplaceSubstring {
    // Method to replace all occurrences of oldSub with newSub in str
    public String replaceSubstring(String str, String oldSub, String newSub) {
        // Handle edge cases
        if (str == null || oldSub == null || newSub == null || oldSub.isEmpty()) {
            return str;
        }

        StringBuilder replaced = new StringBuilder();
        int startIndex = 0;
        int findIndex;

        // Loop through the string finding all occurrences of oldSub
        while ((findIndex = str.indexOf(oldSub, startIndex)) != -1) {
            // Append the portion from startIndex to findIndex
            replaced.append(str.substring(startIndex, findIndex));
            // Append the replacement string
            replaced.append(newSub);
            // Move startIndex to after the replaced substring
            startIndex = findIndex + oldSub.length();
        }

        // Append the remaining portion of the string
        if (startIndex < str.length()) {
            replaced.append(str.substring(startIndex));
        }

        return replaced.toString();
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources
            ReplaceSubstring obj = new ReplaceSubstring();

            System.out.print("Enter the main string: ");
            String str = sc.nextLine();

            System.out.print("Enter the substring to replace: ");
            String oldSub = sc.nextLine();

            System.out.print("Enter the new substring: ");
            String newSub = sc.nextLine();

            String result = obj.replaceSubstring(str, oldSub, newSub);
            System.out.println("Modified string: " + result);
        }
    }
}