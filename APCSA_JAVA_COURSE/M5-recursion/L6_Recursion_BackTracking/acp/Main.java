import java.util.Scanner;

public class Main {

    public static void printTargetSumSubsets(int[] arr, int index, String set, int sum, int target) {

        // Base case
        if (index == arr.length) {
            if (sum == target) {
                System.out.println(set + ".");
            }
            return;
        }

        // Include the current element
        printTargetSumSubsets(arr, index + 1,
                set + arr[index] + ", ",
                sum + arr[index],
                target);

        // Exclude the current element
        printTargetSumSubsets(arr, index + 1,
                set,
                sum,
                target);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Read number of elements
        int n = sc.nextInt();

        int[] arr = new int[n];

        // Read array elements
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Read target
        int target = sc.nextInt();

        // Print target sum subsets
        printTargetSumSubsets(arr, 0, "", 0, target);

        sc.close();
    }
}