import java.util.Scanner;

public class Main {

    // Merge Sort function
    public static int mergeSort(int[] arr, int left, int right) {
        if (left >= right) {
            return 0;
        }

        int mid = (left + right) / 2;

        int count = mergeSort(arr, left, mid);
        count += mergeSort(arr, mid + 1, right);
        count += countPairs(arr, left, mid, right);

        merge(arr, left, mid, right);

        return count;
    }

    // Count reverse pairs
    public static int countPairs(int[] arr, int left, int mid, int right) {
        int count = 0;
        int j = mid + 1;

        for (int i = left; i <= mid; i++) {
            while (j <= right && arr[i] > 2L * arr[j]) {
                j++;
            }
            count += (j - (mid + 1));
        }

        return count;
    }

    // Merge two sorted halves
    public static void merge(int[] arr, int left, int mid, int right) {
        int[] temp = new int[right - left + 1];

        int i = left;
        int j = mid + 1;
        int k = 0;

        while (i <= mid && j <= right) {
            if (arr[i] <= arr[j]) {
                temp[k++] = arr[i++];
            } else {
                temp[k++] = arr[j++];
            }
        }

        while (i <= mid) {
            temp[k++] = arr[i++];
        }

        while (j <= right) {
            temp[k++] = arr[j++];
        }

        for (i = left, k = 0; i <= right; i++, k++) {
            arr[i] = temp[k];
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Read array size
        int n = sc.nextInt();
        int[] nums = new int[n];

        // Read array elements
        for (int i = 0; i < n; i++) {
            nums[i] = sc.nextInt();
        }

        int result = mergeSort(nums, 0, n - 1);

        System.out.println("Number of Reverse Pairs: " + result);

        sc.close();
    }
}
