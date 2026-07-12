public class Main {

    // Recursive method to print Zig-Zag pattern
    public static void printZigZag(int n) {
        if (n == 0) {
            return;
        }

        System.out.println("Pre " + n);
        printZigZag(n - 1);

        System.out.println("In " + n);
        printZigZag(n - 1);

        System.out.println("Post " + n);
    }

    public static void main(String[] args) {
        int n = 2;
        printZigZag(n);
    }
}