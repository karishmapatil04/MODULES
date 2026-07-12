import java.util.Scanner;

public class RotateByNinyety {
    // Main method - Entry point of the program
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Prompt the user to enter the size of the matrix (n x n)
        System.out.print("Enter the size of the matrix (n x n): ");
        int n = scn.nextInt();

        // Initialize a 2D array to store the matrix elements
        int[][] arr = new int[n][n];

        // Prompt the user to enter the elements of the matrix
        System.out.println("Enter the elements of the " + n + "x" + n + " matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                arr[i][j] = scn.nextInt(); // Store each element
            }
        }

        // Call the function to rotate the matrix by 90 degrees
        rotateBy90(arr);

        // Display the rotated matrix
        System.out.println("The rotated matrix is:"); // Added this print statement
        display(arr);
    }

    // Function to rotate the matrix by 90 degrees clockwise
    public static void rotateBy90(int[][] arr) {
        // Step 1: Transpose the matrix (swap rows with columns)
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                // Swap arr[i][j] with arr[j][i]
                int temp = arr[i][j];
                arr[i][j] = arr[j][i];
                arr[j][i] = temp;
            }
        }

        // Step 2: Reverse each row
        for (int i = 0; i < arr.length; i++) {
            int left = 0;
            int right = arr[i].length - 1;

            // Reverse the row (swap left and right elements)
            while (left < right) {
                int temp = arr[i][left];
                arr[i][left] = arr[i][right];
                arr[i][right] = temp;
                left++;
                right--;
            }
        }
    }

    // Function to display the matrix
    public static void display(int[][] arr) {
        // Iterate through the rows and columns to display the matrix
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.print(arr[i][j] + " "); // Print each element
            }
            System.out.println(); // Move to the next line after each row
        }
    }
}