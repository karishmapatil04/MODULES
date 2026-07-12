import java.util.Scanner;

public class DiagonalTraversal {
    // Main method - Entry point of the program
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Prompt the user to enter the size of the matrix (n x n)
        System.out.print("Enter the size of the matrix (n x n): ");
        int n = scn.nextInt();

        // Initialize a 2D array (matrix) of size n x n
        int[][] arr = new int[n][n];

        // Prompt the user to enter the elements of the matrix
        System.out.println("Enter the elements of the " + n + "x" + n + " matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = scn.nextInt(); // Store each element in the array
            }
        }

        // Print the text before displaying the diagonals
        System.out.println("The diagonally traversed matrix:");

        // Print the diagonal elements starting from row 0
        for (int move = 0; move < n; move++) {
            int i = 0;
            int j = move;
            while (i < n && j < n) {
                System.out.print(arr[i][j] + " ");
                i++;
                j++;
            }
            System.out.println(); // Move to the next line after printing the diagonal
        }

        // Continue printing diagonals starting from column 1 (except the first row)
        for (int move = 1; move < n; move++) {
            int i = move;
            int j = 0;
            while (i < n && j < n) {
                System.out.print(arr[i][j] + " ");
                i++;
                j++;
            }
            System.out.println(); // Move to the next line after printing the diagonal
        }
    }
}