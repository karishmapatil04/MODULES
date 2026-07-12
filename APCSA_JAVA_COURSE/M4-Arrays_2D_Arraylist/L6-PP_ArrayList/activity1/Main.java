
// Importing necessary libraries for input/output and ArrayList handling
import java.util.*;

public class ArrayListTrial {

    // Main method where the execution starts
    public static void main(String[] args) {

        // Creating a Scanner object to read input from the user
        Scanner sc = new Scanner(System.in);

        // Prompting user to input the number of arrays (n)
        System.out.print("Enter the number of arrays you want to input: ");
        int n = sc.nextInt();

        // Creating a 2D ArrayList to store multiple ArrayList objects of integers
        ArrayList<ArrayList<Integer>> list = new ArrayList<>();

        // Loop through to input each sub-array
        for (int i = 0; i < n; i++) {
            // Prompting user to input the size of the current sub-array (n1)
            System.out.print("Enter the size of array " + (i + 1) + ": ");
            int n1 = sc.nextInt();

            // Creating a new ArrayList to store the elements of the sub-array
            ArrayList<Integer> l2 = new ArrayList<>();

            // Prompting user to input the elements of the current sub-array and adding to
            // l2
            System.out.println("Enter the " + n1 + " elements of array " + (i + 1) + ": ");
            for (int j = 0; j < n1; j++) {
                l2.add(sc.nextInt());
            }

            // Adding the sub-array to the main ArrayList at index i
            list.add(i, l2);
        }

        // Prompting user to input the number of queries to process (num)
        System.out.print("Enter the number of queries to process: ");
        int num = sc.nextInt();

        // Loop through for each query
        for (int k = 0; k < num; k++) {
            // Prompting user to input the row (n) and column (o) for the current query
            System.out.print("Enter row and column for query " + (k + 1) + ": ");
            int m = sc.nextInt();
            int o = sc.nextInt();

            try {
                // Trying to print the element at the specified row and column
                System.out.println("Element at (" + m + ", " + o + "): " + list.get(m - 1).get(o - 1));
            } catch (Exception e) {
                // If an exception occurs (index out of bounds), print ERROR
                System.out.println("ERROR!");
            }
        }
    }
}
