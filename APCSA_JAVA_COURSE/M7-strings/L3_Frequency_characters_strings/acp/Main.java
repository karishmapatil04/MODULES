import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Input email ID
        System.out.print("Enter an email ID: ");
        String email = sc.nextLine();

        int[] digitFreq = new int[10];
        int atCount = 0;
        int dotCount = 0;
        int underscoreCount = 0;
        int hyphenCount = 0;
        int otherSpecialCount = 0;

        // Count frequencies
        for (int i = 0; i < email.length(); i++) {
            char ch = email.charAt(i);

            if (Character.isDigit(ch)) {
                digitFreq[ch - '0']++;
            } else if (!Character.isLetter(ch)) {
                switch (ch) {
                    case '@':
                        atCount++;
                        break;
                    case '.':
                        dotCount++;
                        break;
                    case '_':
                        underscoreCount++;
                        break;
                    case '-':
                        hyphenCount++;
                        break;
                    default:
                        otherSpecialCount++;
                }
            }
        }

        // Display digit frequencies
        System.out.println("Frequency of Numeric Characters:");
        for (int i = 0; i < 10; i++) {
            if (digitFreq[i] > 0) {
                System.out.println(i + " --> " + digitFreq[i]);
            }
        }

        // Display special character frequencies
        System.out.println("\nFrequency of Special Characters:");
        if (atCount > 0)
            System.out.println("@ --> " + atCount);
        if (dotCount > 0)
            System.out.println(". --> " + dotCount);
        if (underscoreCount > 0)
            System.out.println("_ --> " + underscoreCount);
        if (hyphenCount > 0)
            System.out.println("- --> " + hyphenCount);
        if (otherSpecialCount > 0)
            System.out.println("Other Special Characters --> " + otherSpecialCount);

        sc.close();
    }
}