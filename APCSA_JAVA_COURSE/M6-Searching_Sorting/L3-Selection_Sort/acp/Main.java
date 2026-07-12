import java.util.Scanner;

public class Main {

    // Selection Sort
    public static void selectionSort(int[] arr) {
        int n = arr.length;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < n; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }

            // Swap
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Input array size
        int n = sc.nextInt();

        int[] original = new int[n];
        int[] sorted = new int[n];

        // Input elements
        for (int i = 0; i < n; i++) {
            original[i] = sc.nextInt();
            sorted[i] = original[i];
        }

        // Sort the copied array
        selectionSort(sorted);

        // Print the sorted position of each original element
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (original[i] == sorted[j]) {
                    System.out.println(original[i] + " -> Position " + j);
                    break;
                }
            }
        }

        sc.close();
    }
}
