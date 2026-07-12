import java.util.*;

public class TowerofHanoi {

    // Recursive method to solve the Tower of Hanoi problem
    public static void toh(int n, int t1, int t2, int t3) {
        // Base case: if no disks left, return
        if (n == 0) {
            return;
        }

        // Move n-1 disks from t1 to t3 using t2 as auxiliary
        toh(n - 1, t1, t3, t2);

        // Move the nth disk from t1 to t2
        System.out.println("Move disk " + n + " from Tower " + t1 + " to Tower " + t2);

        // Move the n-1 disks from t3 to t2 using t1 as auxiliary
        toh(n - 1, t3, t2, t1);
    }

    // Main method - Entry point of the program
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Ask the user to input the number of disks
        System.out.print("Enter the number of disks: ");
        int n = scn.nextInt();

        // Ask the user to input the numbers for the three towers (e.g., 1, 2, 3 for
        // Tower 1, Tower 2, and Tower 3)
        System.out.print("Enter the number for the first tower (t1): ");
        int t1 = scn.nextInt();

        System.out.print("Enter the number for the second tower (t2): ");
        int t2 = scn.nextInt();

        System.out.print("Enter the number for the third tower (t3): ");
        int t3 = scn.nextInt();

        // Call the toh method to solve the Tower of Hanoi problem
        toh(n, t1, t2, t3);
    }
}