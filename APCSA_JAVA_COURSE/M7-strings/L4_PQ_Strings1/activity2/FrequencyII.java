import java.util.Scanner;

public class FrequencyII {
    // Method to count occurrences of a substring (sub) in the main string (str)
    public int countSubstring(String str, String sub) {
        int count = 0;
        int index = 0;
        // Loop to find all occurrences of the substring
        while (index >= 0) {
            // Find the index of the substring starting from 'index'
            index = str.indexOf(sub, index);
            if (index >= 0) {
                count++; // Increment count if the substring is found
                index += sub.length(); // Move index forward by the length of the substring
            }
        }
        return count; // Return the total count of the substring occurrences
    }

    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner sc = new Scanner(System.in);
        FrequencyII obj = new FrequencyII();

        // Prompt the user for the main string (str)
        System.out.print("Enter the main string: ");
        String str = sc.nextLine();

        // Prompt the user for the substring (sub)
        System.out.print("Enter the substring to count: ");
        String sub = sc.nextLine();

        // Call the countSubstring method to find the number of occurrences
        int result = obj.countSubstring(str, sub);

        // Print the result
        System.out.println("The substring \"" + sub + "\" appears " + result + " times in the main string.");
    }
}