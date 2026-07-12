import java.util.*;

public class ReverseString {

    // Function to reverse the entire string (for single words and multiple words)
    static String reverseString(String str) {
        // Convert the string to a character array to perform the reversal
        char[] ch = str.toCharArray();
        int start = 0;
        int end = ch.length - 1;

        // Reversing the entire string
        while (start < end) {
            char temp = ch[start];
            ch[start] = ch[end];
            ch[end] = temp;
            start++;
            end--;
        }
        return new String(ch); // Convert the char array back to a string
    }

    // Function to reverse the words and the order of words in a sentence
    static String reverseWordsAndSentence(String sentence) {
        String[] words = sentence.split(" ");
        StringBuilder reversedSentence = new StringBuilder();

        // Reverse the order of words and reverse each word's letters
        for (int i = words.length - 1; i >= 0; i--) {
            reversedSentence.append(reverseString(words[i])).append(" ");
        }

        return reversedSentence.toString().trim(); // Remove the trailing space
    }

    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);

        System.out.print("Enter a string to reverse its words and sentence: ");
        String input = scn.nextLine();

        // If there's only one word, reverse the entire string
        if (input.split(" ").length == 1) {
            String reversedString = reverseString(input);
            System.out.println("Reversed string: " + reversedString);
        } else {
            String reversedWordsAndSentence = reverseWordsAndSentence(input);
            System.out.println("Reversed string: " + reversedWordsAndSentence);
        }
    }
}