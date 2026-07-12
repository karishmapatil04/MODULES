import java.util.Scanner;

public class StringFrequencyI {

    // Method to check if str2 is a substring of str1
    // Returns true if str2 is found in str1, otherwise false
    public boolean isSubstring(String str1, String str2) {
        // Check if str2 exists in str1 using the indexOf method
        int index = str1.indexOf(str2);
        // If index is greater than or equal to 0, the substring exists
        return index >= 0;
    }

    // Main method to test the isSubstring function
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringFrequencyI obj = new StringFrequencyI();

        // Taking user input for the main string (str1)
        System.out.print("Enter the main string (str1): ");
        String str1 = sc.nextLine();

        // Taking user input for the substring (str2)
        System.out.print("Enter the substring (str2): ");
        String str2 = sc.nextLine();

        // Check if str2 is a substring of str1 and print the result
        if (obj.isSubstring(str1, str2)) {
            System.out.println("\"" + str2 + "\" is a substring of \"" + str1 + "\"");

        } else {
            System.out.println("\"" + str2 + "\" is not a substring of \"" + str1 + "\"");
        }
    }
}