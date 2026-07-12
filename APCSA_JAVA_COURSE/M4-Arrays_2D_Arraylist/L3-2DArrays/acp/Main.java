public class Main {
    public static void main(String[] args) {

        // First matrix (2x2)
        int[][] matrix1 = {
                { 1, 2 },
                { 3, 4 }
        };

        // Second matrix (2x2)
        int[][] matrix2 = {
                { 5, 6 },
                { 7, 8 }
        };

        // Result matrix
        int[][] result = new int[2][2];

        // Matrix multiplication
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                result[i][j] = 0;
                for (int k = 0; k < 2; k++) {
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }

        // Display the result
        System.out.println("Result of Matrix Multiplication:");
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}
