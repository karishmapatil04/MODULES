import java.util.ArrayList;
import java.util.List;

public class Subsets {
    // List to store the resulting subsets
    List<List<Integer>> output = new ArrayList<>();

    // Main method to return the subsets of the input array
    public List<List<Integer>> subsets(int[] nums) {
        int n = nums.length;
        // Call the helper function to generate the subsets
        helper(0, new ArrayList<Integer>(), nums);
        return output;
    }

    // Helper function to generate subsets using backtracking
    public void helper(int first, ArrayList<Integer> curr, int[] nums) {
        // If we've considered all elements, add the current subset to output
        if (first == nums.length) {
            output.add(new ArrayList<>(curr));
            return;
        }

        // Exclude the current element and move on to the next element
        helper(first + 1, curr, nums);

        // Include the current element in the subset and move on to the next element
        curr.add(nums[first]);
        helper(first + 1, curr, nums);

        // Backtrack: remove the current element and explore other possibilities
        curr.remove(curr.size() - 1);
    }

    public static void main(String[] args) {
        // Example usage
        Subsets solution = new Subsets();
        int[] nums = { 1, 2, 3 };
        List<List<Integer>> result = solution.subsets(nums);
        System.out.println(result);
    }
}