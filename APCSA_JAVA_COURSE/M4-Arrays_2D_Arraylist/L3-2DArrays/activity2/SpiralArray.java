import java.util.Scanner;

public class SpiralArray {

    // Main method - Entry point of the program
    public static void main(String[] args) {

        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Ask the user to enter the number of rows (n) and columns (m)
        System.out.print("Enter the number of rows: ");
        int n = scn.nextInt();
        System.out.print("Enter the number of columns: ");
        int m = scn.nextInt();

        // Handle case where array dimensions are 0
        if (n == 0 || m == 0) {
            System.out.println("Array dimensions cannot be zero.");
            return;
        }

        // Create a 2D array to store the elements
        int[][] arr = new int[n][m];

        // Ask the user to enter the elements of the 2D array
        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = scn.nextInt(); // Store each input value in the array
            }
        }

        // Initialize boundaries for the spiral traversal
        int rmin = 0, cmin = 0, rmax = n - 1, cmax = m - 1;
        int count = 0;

        // Start the spiral traversal
        System.out.println("Spiral order traversal of the array:");
        while (count < n * m) {
            // Traverse the top row (left to right)
            for (int col = cmin; col <= cmax && count < n * m; col++) {
                System.out.print(arr[rmin][col] + " ");
                count++;
            }
            rmin++;

            // Traverse the right column (top to bottom)
            for (int row = rmin; row <= rmax && count < n * m; row++) {
                System.out.print(arr[row][cmax] + " ");
                count++;
            }
            cmax--;

            // Traverse the bottom row (right to left)
            for (int col = cmax; col >= cmin && count < n * m; col--) {
                System.out.print(arr[rmax][col] + " ");
                count++;
            }
            rmax--;

            // Traverse the left column (bottom to top)
            for (int row = rmax; row >= rmin && count < n * m; row--) {
                System.out.print(arr[row][cmin] + " ");
                count++;
            }
            cmin++;
        }
    }
}
