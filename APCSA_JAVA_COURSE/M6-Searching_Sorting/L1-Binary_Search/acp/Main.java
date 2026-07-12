import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read the size of the array
        int n = sc.nextInt();

        int[] arr = new int[n];

        // Read the sorted array elements
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        // Read the target value
        int d = sc.nextInt();

        int low = 0;
        int high = n - 1;
        int floor = -1;
        int ceil = -1;

        // Binary Search
        while (low <= high) {
            int mid = (low + high) / 2;

            if (arr[mid] == d) {
                floor = arr[mid];
                ceil = arr[mid];
                break;
            } else if (arr[mid] < d) {
                floor = arr[mid];
                low = mid + 1;
            } else {
                ceil = arr[mid];
                high = mid - 1;
            }
        }

        System.out.println("Floor: " + floor);
        System.out.println("Ceil: " + ceil);

        sc.close();
    }
}