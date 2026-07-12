import java.util.Scanner;

public class CountFrequencyArray {
    public static void main(String[] args) {
        // Take input from the user
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the string: ");
        String str = sc.nextLine();
        int[] freq = new int[str.length()]; // Frequency array to store the frequency of each character

        // Convert the given string into character array
        char str1[] = str.toCharArray();

        // Loop through each character in the string
        for (int i = 0; i < str.length(); i++) {
            freq[i] = 1;

            // Compare with subsequent characters
            for (int j = i + 1; j < str.length(); j++) {
                if (str1[i] == str1[j]) // If the characters are the same
                    freq[i]++;
            }
        }

        // Display the characters and their corresponding frequency
        System.out.println("Frequencies of the characters in the string are as below: ");
        System.out.println("Characters Frequencies");

        // Loop through and display the frequencies
        for (int i = 0; i < freq.length; i++) {
            if (str1[i] != '&' && str1[i] != '0') // Skip spaces and already processed characters
                System.out.println(str1[i] + " " + freq[i]);
        }
    }
}