public class Main {
    public static void main(String[] args) {

        // Original array
        int[] arr = { 4, 0, 2, 3, 1 };

        // Inverse array
        int[] inverse = new int[arr.length];

        // Find the inverse
        for (int i = 0; i < arr.length; i++) {
            inverse[arr[i]] = i;
        }

        // Display original array
        System.out.print("Original Array: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        System.out.println();

        // Display inverse array
        System.out.print("Inverse Array: ");
        for (int num : inverse) {
            System.out.print(num + " ");
        }
    }
}