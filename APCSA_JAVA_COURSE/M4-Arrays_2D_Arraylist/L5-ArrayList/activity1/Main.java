import java.util.*;

public class RemovePrime {

    // Method to remove all prime numbers from the ArrayList
    public static void solution(ArrayList<Integer> al) {
        // Looping through the list in reverse order to safely remove elements
        for (int i = al.size() - 1; i >= 0; i--) {
            // Check if the current element is prime
            if (isPrime(al.get(i)) == true) {
                // Remove the prime element from the list
                al.remove(i);
            }
        }
    }

    // Method to check if a number is prime
    public static boolean isPrime(int n) {
        if (n <= 1) {
            return false; // 1 and negative numbers are not prime
        }
        // Loop to check divisibility up to the square root of n
        for (int c = 2; c <= n; c++) {
            if (n % c == 0) {
                // If n is divisible by any number other than 1 and itself, it's not prime
                return false;
            }
        }
        // If no divisors are found, the number is prime
        return true;
    }

    // Main method (entry point of the program)
    public static void main(String[] args) {

        // Creating Scanner object to read input
        Scanner scan = new Scanner(System.in);

        // Reading the number of elements in the ArrayList
        System.out.print("Enter the number of integers you want to input: ");
        int n = scan.nextInt();

        // Creating an ArrayList to store the integers
        ArrayList<Integer> al = new ArrayList<>();

        // Reading the integers into the ArrayList
        System.out.println("Enter the " + n + " integers:");
        for (int i = 0; i < n; i++) {
            al.add(scan.nextInt());
        }

        // Calling the solution method to remove primes
        solution(al);

        // Printing the modified list after removing primes
        System.out.println("Modified list (without primes): " + al);
    }
}
