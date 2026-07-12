import java.util.Scanner;

public class FibonacciSeries {

    // Static variables to store Fibonacci series values
    static int n1 = 0, n2 = 1, n3 = 0;

    // Method to print Fibonacci series up to the given count
    static void printFibonacci(int count) {
        if (count > 0) {
            // Calculate the next Fibonacci number
            n3 = n1 + n2;

            // Update n1 and n2 for the next iteration
            n1 = n2;
            n2 = n3;

            // Print the current Fibonacci number
            System.out.print(" " + n3);

            // Recursive call to print the next Fibonacci number
            printFibonacci(count - 1);
        }
    }

    // Main method - Entry point of the program
    public static void main(String args[]) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Ask the user how many Fibonacci numbers they want to print
        System.out.print("Enter the number of Fibonacci numbers you want to print: ");
        int count = scn.nextInt(); // Read the input

        // Print the first two Fibonacci numbers
        System.out.print(n1 + " " + n2);

        // Call the printFibonacci method to print the next Fibonacci numbers
        printFibonacci(count - 2); // Subtract 2 because 0 and 1 are already printed
    }
}