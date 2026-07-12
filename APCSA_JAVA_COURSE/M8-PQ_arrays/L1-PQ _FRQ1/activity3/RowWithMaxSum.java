import java.util.Scanner;

public class RowWithMaxSum {
    // Method to get the row with the maximum sum from a 2D array
    public static int[] getRowWithMaxSum(int[][] array2D) {
        int[] maxRow = array2D[0]; // Initially, set the first row as the max row
        int maxSum = 0;

        // Loop through all rows in the 2D array
        for (int i = 0; i < array2D.length; i++) {
            int sum = 0;

            // Calculate the sum of the current row
            for (int j = 0; j < array2D[i].length; j++) {
                sum += array2D[i][j];
            }

            // If the current row's sum is greater than the max sum, update the max sum and
            // max row
            if (sum > maxSum) {
                maxSum = sum;
                maxRow = array2D[i];
            }
        }

        return maxRow; // Return the row with the maximum sum
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources to automatically close the scanner
            // Ask the user to input the number of rows and columns for the 2D array
            System.out.print("Enter the number of rows in the array: ");
            int rows = sc.nextInt();
            System.out.print("Enter the number of columns in the array: ");
            int cols = sc.nextInt();

            // Create the 2D array based on user input
            int[][] array2D = new int[rows][cols];

            // Ask the user to input the elements of the 2D array
            System.out.println("Enter the elements of the 2D array:");
            for (int i = 0; i < rows; i++) {
                for (int j = 0; j < cols; j++) {
                    array2D[i][j] = sc.nextInt();
                }
            }

            // Call the method to get the row with the maximum sum
            int[] result = getRowWithMaxSum(array2D);

            // Print the row with the maximum sum
            System.out.println("The row with the maximum sum is: ");
            for (int num : result) {
                System.out.print(num + " ");
            }
        }
    }
}