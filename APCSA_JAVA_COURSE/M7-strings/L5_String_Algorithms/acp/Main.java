import java.util.Scanner;

public class Main {

    // Function to count occurrences of pattern in text
    public static int countOccurrences(String pattern, String text) {
        int count = 0;

        for (int i = 0; i <= text.length() - pattern.length(); i++) {
            if (text.substring(i, i + pattern.length()).equals(pattern)) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input pattern and text
        String pattern = sc.nextLine();
        String text = sc.nextLine();

        int result = countOccurrences(pattern, text);

        System.out.println(result);

        sc.close();
    }
}