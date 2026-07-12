import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Input the string
        System.out.println("Enter a sentence:");
        String str = sc.nextLine().toLowerCase();

        boolean[] alphabet = new boolean[26];

        // Mark the letters present in the string
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                alphabet[ch - 'a'] = true;
            }
        }

        // Check if all letters are present
        boolean isPangram = true;

        for (int i = 0; i < 26; i++) {
            if (!alphabet[i]) {
                isPangram = false;
                break;
            }
        }

        // Display the result
        if (isPangram) {
            System.out.println("The given string is a Pangram.");
        } else {
            System.out.println("The given string is not a Pangram.");
        }

        sc.close();
    }
}