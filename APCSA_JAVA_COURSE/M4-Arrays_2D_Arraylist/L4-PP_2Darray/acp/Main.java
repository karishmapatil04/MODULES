public class Main {
    public static void main(String[] args) {

        // 3x3 matrix
        int[][] matrix = {
                { 3, 8, 7 },
                { 5, 2, 9 },
                { 6, 1, 4 }
        };

        boolean found = false;

        // Find the saddle point
        for (int i = 0; i < matrix.length; i++) {

            // Find the minimum element in the current row
            int minCol = 0;
            for (int j = 1; j < matrix[i].length; j++) {
                if (matrix[i][j] < matrix[i][minCol]) {
                    minCol = j;
                }
            }

            // Check if it is the largest in its column
            boolean saddlePoint = true;
            for (int k = 0; k < matrix.length; k++) {
                if (matrix[k][minCol] > matrix[i][minCol]) {
                    saddlePoint = false;
                    break;
                }
            }

            if (saddlePoint) {
                System.out.println("Saddle Point: " + matrix[i][minCol]);
                found = true;
                break;
            }
        }

        if (!found) {
            System.out.println("No Saddle Point Found.");
        }
    }
}