
// Importing necessary libraries for input/output and ArrayList handling
import java.util.*;

// Define the main class 'ReverseList' where the program logic is implemented
class ReverseList {

    // Main method - Entry point of the program
    public static void main(String[] args) {
        // Create a Scanner object to read input from the user
        Scanner scn = new Scanner(System.in);

        // Ask the user to enter the number of elements to input into the list
        System.out.print("Enter the number of elements in the list: ");
        int n = scn.nextInt();

        // Create an ArrayList to store the integers
        ArrayList<Integer> al = new ArrayList<>();

        // Ask the user to enter the integers and add them to the ArrayList
        System.out.println("Enter the " + n + " integers:");
        for (int i = 0; i < n; i++) {
            al.add(scn.nextInt()); // Add each input value to the list
        }

        // Call the reverse method to reverse the ArrayList and store the result in
        // 'ans'
        ArrayList<Integer> ans = reverse(al);

        // Print the reversed ArrayList
        System.out.println("Reversed List: " + ans);
    }

    // Method to reverse the given ArrayList
    static ArrayList<Integer> reverse(ArrayList<Integer> list) {
        // Create a new ArrayList to store the reversed list
        ArrayList<Integer> ans = new ArrayList<>();

        // Loop through the list in reverse order and add the elements to the new
        // ArrayList
        for (int i = list.size() - 1; i >= 0; i--) {
            ans.add(list.get(i)); // Add each element to the reversed list
        }

        // Return the reversed ArrayList
        return ans;
    }
}
