import java.util.Scanner;

public class RingRotate {

    // Main method - Entry point of the program
    public static void main(String[] args) throws Exception {

        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Prompt the user to enter the number of rows and columns
        System.out.print("Enter the number of rows: ");

        int n = scn.nextInt();

        System.out.print("Enter the number of columns: ");

        int m = scn.nextInt();

        // Create a 2D array to store the matrix elements
        int[][] arr = new int[n][m];

        // Prompt the user to enter the elements of the matrix
        System.out.println("Enter the elements of the " + n + "x" + m + " matrix:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                arr[i][j] = scn.nextInt(); // Store each element
            }
        }

        // Prompt the user to enter the ring number (sno) and the rotation number (rno)
        System.out.print("Enter the ring number (sno): ");

        int sno = scn.nextInt();

        System.out.print("Enter the number of rotations (rno): ");

        int rno = scn.nextInt();

        // Call the ring rotation function
        ringrotate(arr, sno, rno);

        // Display the updated matrix
        display(arr);
    }

    // Function to perform the rotation on the specified ring
    public static void ringrotate(int[][] arr, int sno, int rno) {
        // Convert the 2D ring into a 1D array
        int[] la = fill1Dfrom2D(arr, sno);

        // Rotate the 1D array
        rotate1D(la, rno);

        // Fill the 2D array back from the 1D array
        fill2Dfrom1D(arr, la, sno);
    }

    // Function to convert the 2D ring to a 1D array

    public static int[] fill1Dfrom2D(int[][] arr, int sno) {
        int rmin = sno - 1;
        int cmin = sno - 1;
        int rmax = arr.length - sno;

        int cmax = arr[0].length - sno;
        // Total size of the ring
        int sz = 2 * (rmax - rmin + cmax - cmin);

        int[] la = new int[sz];
        int idx = 0;

        // Traverse the ring and fill the 1D array
        for (int row = rmin; row <= rmax; row++) {
            la[idx] = arr[row][cmin];
            idx++;
        }

        cmin++;

        for (int col = cmin; col <= cmax; col++) {
            la[idx] = arr[rmax][col];
            idx++;
        }

        rmax--;

        for (int row = rmax; row >= rmin; row--) {
            la[idx] = arr[row][cmax];
            idx++;
        }

        cmax--;

        for (int col = cmax; col >= cmin; col--) {
            la[idx] = arr[rmin][col];
            idx++;
        }

        rmin++;

        return la;
    }

    // Function to rotate the 1D array by the given number of steps (rno)
    public static void rotate1D(int[] la, int rno) {
        rno = rno % la.length;

        if (rno < 0) {
            rno += la.length;
        }

        reverse(la, 0, la.length - 1);
        reverse(la, 0, rno - 1);
        reverse(la, rno, la.length - 1);
    }

    // Function to reverse a portion of the array
    public static void reverse(int[] la, int left, int right) {
        while (left < right) {
            int temp = la[left];
            la[left] = la[right];
            la[right] = temp;
            left++;
            right--;
        }
    }

    // Function to fill the 2D array back from the 1D array after rotation
    public static void fill2Dfrom1D(int[][] arr, int[] la, int sno) {

        int rmin = sno - 1;

        int cmin = sno - 1;

        int rmax = arr.length - sno;

        int cmax = arr[0].length - sno;

        int idx = 0;

        // Fill the 2D array back from the 1D array
        for (int row = rmin; row <= rmax; row++) {
            arr[row][cmin] = la[idx];
            idx++;
        }

        cmin++;

        for (int col = cmin; col <= cmax; col++) {

            arr[rmax][col] = la[idx];
            idx++;
        }

        rmax--;

        for (int row = rmax; row >= rmin; row--) {

            arr[row][cmax] = la[idx];
            idx++;
        }

        cmax--;

        for (int col = cmax; col >= cmin; col--) {
            arr[rmin][col] = la[idx];
            idx++;
        }

        rmin++;
    }

    // Function to display the 2D array
    public static void display(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}