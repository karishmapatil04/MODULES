import java.util.ArrayList;
import java.util.Scanner;

public class FindFactors {
    // Method to find all factors of a given number
    public ArrayList<Integer> findFactors(int number) {
        // Create an ArrayList to store the factors
        ArrayList<Integer> factors = new ArrayList<>();

        // Loop through all numbers from 1 to the given number
        for (int i = 1; i <= number; i++) {
            // If the number is divisible by i, add it to the factors list
            if (number % i == 0) {
                factors.add(i);
            }
        }

        // Return the list of factors
        return factors;
    }

    // Main method - Entry point of the program
    public static void main(String[] args) {
        // Create a Scanner object to read user input
        Scanner sc = new Scanner(System.in);

        // Ask the user to input a number
        System.out.print("Enter a number to find its factors: ");
        int number = sc.nextInt();

        // Create an object of FindFactors class
        FindFactors obj = new FindFactors();

        // Call the findFactors method and get the factors
        ArrayList<Integer> factors = obj.findFactors(number);

        // Print the factors
        System.out.println("Factors of " + number + ": " + factors);
    }
}