import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner sc = new Scanner(System.in);

        // Prompt the user for the first string
        System.out.print("Enter the first string: ");
        String s1 = sc.nextLine();
        System.out.println("For " + s1);
        frequency(s1);

        // Prompt the user for the second string
        System.out.print("Enter the second string: ");
        String s2 = sc.nextLine();
        System.out.println("For " + s2);
        frequency(s2);
    }

    // Method to calculate and print the frequency of characters in a given string
    private static void frequency(String s) {
        // Check if the string is empty
        if (s.length() == 0) {
            System.out.println("Empty string");
            return;
        }

        // Create an ArrayList to store occurrences of characters
        ArrayList<CharOccur> occurrences = new ArrayList<CharOccur>();

        // Loop through each character in the string
        for (int i = 0; i < s.length(); i++) {
            // Get the character at position i
            char c = s.charAt(i);
            int flag = 0;

            // Check if the character is already present in the occurrences list
            for (CharOccur o : occurrences) {
                if (o.character == c) {
                    o.occurrence += 1; // Increment occurrence if character already exists
                    flag = 1;
                }
            }

            // If the character was not found, create a new CharOccur object for it
            if (flag == 0) {
                CharOccur grp = new CharOccur(c, 1);
                occurrences.add(grp);
            }
        }

        // Print the frequency of each character
        for (CharOccur o : occurrences) {
            System.out.println(o.character + " " + o.occurrence);
        }
    }
}

// Class to store each character and its occurrence count
class CharOccur {
    // Character and its occurrence
    char character;
    int occurrence = 0;

    // Constructor to initialize character and occurrence
    CharOccur(char character, int occurrence) {
        this.character = character;
        this.occurrence = occurrence;
    }
}
