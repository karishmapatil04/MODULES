import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Input number of characters
        System.out.print("Enter the number of characters: ");
        int n = sc.nextInt();

        ArrayList<Character> chars = new ArrayList<>();

        // Input characters
        System.out.println("Enter the characters:");
        for (int i = 0; i < n; i++) {
            chars.add(sc.next().charAt(0));
        }

        // Construct the string
        StringBuilder str = new StringBuilder();
        for (char ch : chars) {
            str.append(ch);
        }

        System.out.println("Generated String: " + str);

        // Find the length
        System.out.println("Length: " + str.length());

        // Reverse the string
        String reversed = str.reverse().toString();
        System.out.println("Reversed String: " + reversed);

        // Restore the original string
        str.reverse();

        // Split into two equal words
        if (str.length() % 2 == 0) {
            int mid = str.length() / 2;
            String word1 = str.substring(0, mid);
            String word2 = str.substring(mid);

            System.out.println("Word 1: " + word1);
            System.out.println("Word 2: " + word2);
        } else {
            System.out.println("Cannot split into two equal-length words because the string length is odd.");
        }

        sc.close();
    }
}
