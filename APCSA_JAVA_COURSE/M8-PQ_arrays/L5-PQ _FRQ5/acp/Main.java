import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    // Recursive method to generate all letter case permutations
    public static void letterCasePermutation(String s, int index, String current, ArrayList<String> result) {

        // Base case
        if (index == s.length()) {
            result.add(current);
            return;
        }

        char ch = s.charAt(index);

        if (Character.isLetter(ch)) {
            // Lowercase
            letterCasePermutation(s, index + 1,
                    current + Character.toLowerCase(ch), result);

            // Uppercase
            letterCasePermutation(s, index + 1,
                    current + Character.toUpperCase(ch), result);
        } else {
            // Keep digits unchanged
            letterCasePermutation(s, index + 1,
                    current + ch, result);
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Input string
        String s = sc.nextLine();

        ArrayList<String> result = new ArrayList<>();

        // Generate all possible strings
        letterCasePermutation(s, 0, "", result);

        // Display the result
        System.out.println(result);

        sc.close();
    }
}
