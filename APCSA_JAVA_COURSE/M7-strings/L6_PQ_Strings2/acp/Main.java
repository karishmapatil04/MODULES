import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    // Check if a string is a palindrome
    public static boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }

        return true;
    }

    // Recursive function to generate palindrome partitions
    public static void partition(String s, int start, List<String> current, List<List<String>> result) {

        if (start == s.length()) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int end = start + 1; end <= s.length(); end++) {
            String sub = s.substring(start, end);

            if (isPalindrome(sub)) {
                current.add(sub);
                partition(s, end, current, result);
                current.remove(current.size() - 1);
            }
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Input string
        String s = sc.nextLine();

        List<List<String>> result = new ArrayList<>();

        partition(s, 0, new ArrayList<>(), result);

        System.out.println(result);

        sc.close();
    }
}