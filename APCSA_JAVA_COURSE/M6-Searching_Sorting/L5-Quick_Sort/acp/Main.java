import java.util.Scanner;

class Apple {
    int x, y, index;
}

public class Main {

    // Quick Sort
    static void quickSort(Apple[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    static int partition(Apple[] arr, int low, int high) {
        Apple pivot = arr[high];
        int i = low - 1;

        for (int j = low; j < high; j++) {
            if (arr[j].x < pivot.x ||
                    (arr[j].x == pivot.x && arr[j].y < pivot.y)) {

                i++;
                Apple temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        Apple temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        Apple[] apples = new Apple[n];

        for (int i = 0; i < n; i++) {
            apples[i] = new Apple();
            apples[i].x = sc.nextInt();
            apples[i].y = sc.nextInt();
            apples[i].index = i;
        }

        // Sort apples
        quickSort(apples, 0, n - 1);

        int[] eatenBefore = new int[n];

        for (int i = 0; i < n; i++) {
            eatenBefore[apples[i].index] = i;
        }

        for (int i = 0; i < n; i++) {
            System.out.println(eatenBefore[i]);
        }

        sc.close();
    }
}
