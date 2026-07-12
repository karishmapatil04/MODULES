import java.util.Scanner;
import java.util.Arrays;

class CheckAnagram {

    // Function to check whether two strings are anagrams of each other
    static boolean areAnagram(char[] str1, char[] str2) {
        // Get lengths of both strings
        int n1 = str1.length;
        int n2 = str2.length;

        // If length of both strings is not same, they cannot be anagrams
        if (n1 != n2)
            return false;

        // Sort both strings
        Arrays.sort(str1);
        Arrays.sort(str2);

        // Compare sorted strings
        for (int i = 0; i < n1; i++) {
            if (str1[i] != str2[i])
                return false;
        }

        return true; // If all characters match, they are anagrams
    }

    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Ask the user to input the first string
        System.out.println("Enter the first string:");
        String input1 = scn.nextLine();

        // Ask the user to input the second string
        System.out.println("Enter the second string:");
        String input2 = scn.nextLine();

        // Convert the strings to character arrays
        char[] str1 = input1.toCharArray();
        char[] str2 = input2.toCharArray();

        // Check if the strings are anagrams of each other
        if (areAnagram(str1, str2))
            System.out.println("The two strings are anagrams of each other");
        else
            System.out.println("The two strings are not anagrams of each other");
    }
}