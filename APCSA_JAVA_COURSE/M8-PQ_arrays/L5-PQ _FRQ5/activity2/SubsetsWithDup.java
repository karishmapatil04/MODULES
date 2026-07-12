import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Set;
import java.util.HashSet;

public class SubsetsWithDup {
    // A Set to store the subsets without duplicates
    Set<List<Integer>> output = new HashSet<>();

    // Main method to return subsets of the input array, considering duplicates
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        int n = nums.length;

        // Sort the array to handle duplicates efficiently
        Arrays.sort(nums);

        // Call the helper function to generate the subsets
        helper(0, new ArrayList<Integer>(), nums);

        // Convert the set of subsets to a list and return it
        List<List<Integer>> ans = new ArrayList<>(output);
        return ans;
    }

    // Helper function to generate subsets using backtracking
    public void helper(int first, ArrayList<Integer> curr, int[] nums) {
        if (first == nums.length) {
            output.add(new ArrayList<>(curr));
            return;
        }

        // Exclude the current element and move to the next
        helper(first + 1, curr, nums);

        // Include the current element in the subset and move to the next
        curr.add(nums[first]);
        helper(first + 1, curr, nums);

        // Backtrack: remove the current element and explore other possibilities
        curr.remove(curr.size() - 1);
    }

    public static void main(String[] args) {
        // Example usage
        SubsetsWithDup solution = new SubsetsWithDup();
        int[] nums = { 1, 2, 2 };
        List<List<Integer>> result = solution.subsetsWithDup(nums);
        System.out.println(result);
    }
}