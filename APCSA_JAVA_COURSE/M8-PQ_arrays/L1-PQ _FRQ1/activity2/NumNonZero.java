import java.util.Scanner;

public class NumNonZero {
    // Method to count the number of non-zero rows in the 2D array
    public static int numNonZeroRows(int[][] array2D) {
        int count = 0;
        // Iterate through all rows in the 2D array
        for (int i = 0; i < array2D.length; i++) {
            boolean isNonZeroRow = true;
            // Check if the current row contains any zeroes
            for (int j = 0; j < array2D[i].length; j++) {
                if (array2D[i][j] == 0) {
                    isNonZeroRow = false;
                    break; // Exit the loop if zero is found
                }
            }
            // If no zeroes were found in the row, increment the count
            if (isNonZeroRow) {
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) { // Using try-with-resources for automatic closing

            // Ask the user to input the number of rows and columns for the 2D array
            System.out.print("Enter the number of rows in the array: ");
            int rows = scanner.nextInt();
            System.out.print("Enter the number of columns in the array: ");
            int cols = scanner.nextInt();

            // Create a 2D array based on user input
            int[][] array2D = new int[rows][cols];

            // Ask the user to input the elements of the 2D array
            System.out.println("Enter the elements of the 2D array:");
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    array2D[i][j] = scanner.nextInt();
                }
            }

            // Call the method to count the number of non-zero rows
            int result = numNonZeroRows(array2D);

            // Display the result
            System.out.println("The number of non-zero rows is: " + result);
        }
    }
}