import java.util.Scanner;

public class Main {

    // Insertion Sort Method
    public static void insertionSort(int[] arr) {
        int n = arr.length;

        for (int i = 1; i < n; i++) {
            int key = arr[i];
            int j = i - 1;

            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read array size
        int n = sc.nextInt();

        int[] original = new int[n];
        int[] sorted = new int[n];

        // Read array elements
        for (int i = 0; i < n; i++) {
            original[i] = sc.nextInt();
            sorted[i] = original[i];
        }

        // Sort the copied array
        insertionSort(sorted);

        // Find and print the sorted position of each original element
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
