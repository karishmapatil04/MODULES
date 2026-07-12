import java.util.Scanner;

public class Factorial {

    // Main method - Entry point of the program
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Reading the integer input (n) to calculate the factorial
        System.out.print("Enter a number to calculate its factorial: ");
        int n = scn.nextInt();

        // Calling the factorial method and printing the result
        System.out.println("Factorial of " + n + " is: " + factorial(n));
    }

    // Method to calculate the factorial of a number
    public static int factorial(int n) {
        // Base case: if n is 0 or 1, return 1
        if (n == 0 || n == 1) {
            return 1;
        }

        // Recursive case: n * factorial(n-1)
        return n * factorial(n - 1);
    }
}