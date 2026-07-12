public class Main {

    // Recursive method to print all stair paths
    public static void printStairPaths(int n, String path) {
        // Base case: reached the top
        if (n == 0) {
            System.out.println(path);
            return;
        }

        // Base case: invalid path
        if (n < 0) {
            return;
        }

        // Take 1, 2, or 3 steps
        printStairPaths(n - 1, path + "1");
        printStairPaths(n - 2, path + "2");
        printStairPaths(n - 3, path + "3");
    }

    public static void main(String[] args) {
        int stairs = 3;

        System.out.println("Possible Stair Paths:");
        printStairPaths(stairs, "");
    }
}