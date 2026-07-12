import java.util.Scanner;

public class PowerLogarithmic {

    // Main method - Entry point of the program
    public static void main(String[] args) throws Exception {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Ask the user to enter the base (x)
        System.out.print("Enter the base (x): ");
        int x = scn.nextInt();

        // Ask the user to enter the exponent (n)
        System.out.print("Enter the exponent (n): ");
        int n = scn.nextInt();

        // Call the power method to calculate x^n
        int xpn = power(x, n);

        // Print the result
        System.out.println("Result: " + xpn);
    }

    // Method to compute the power using logarithmic time complexity (O(log n))
    public static int power(int x, int n) {
        // Base case: x^0 = 1
        if (n == 0) {
            return 1;
        }

        // Recursive case: Compute power for n/2
        int xpnb2 = power(x, n / 2);

        // Calculate x^n using the result for x^(n/2)
        int xn = xpnb2 * xpnb2;

        // If n is odd, multiply the result by x
        if (n % 2 == 1) {
            xn = xn * x;
        }

        return xn;
    }
}
