import java.util.ArrayList;
import java.util.List;

public class Permutations {
    // List to store the final result
    List<List<Integer>> ans = new ArrayList<>();

    // Main method to generate permutations of the input array
    public List<List<Integer>> permute(int[] nums) {
        // Call the helper function with initial index and an empty list
        helper(0, nums, new ArrayList<>());

        // Return the list of permutations
        return ans;
    }

    // Helper function to generate permutations using backtracking
    public void helper(int idx, int[] nums, ArrayList<Integer> curr) {
        // If the current list has the same length as the input array, we have found a
        // permutation
        if (curr.size() == nums.length) {
            // Add the current permutation to the result
            ans.add(new ArrayList<Integer>(curr));
            return;
        }

        // Iterate through the array to create permutations
        for (int i = idx; i < nums.length; i++) {
            // Add the current element to the permutation list
            curr.add(nums[i]);
            // Swap the current element with the element at the 'idx' position
            swap(nums, i, idx);
            // Recursively generate the next permutations
            helper(idx + 1, nums, curr);
            // Backtrack: undo the swap and remove the last added element
            swap(nums, i, idx);
            curr.remove(curr.size() - 1);
        }
    }

    // Method to swap elements in the array
    public void swap(int[] nums, int i, int idx) {
        // Swap the elements at positions i and idx
        int temp = nums[i];
        nums[i] = nums[idx];
        nums[idx] = temp;
    }

    public static void main(String[] args) {
        // Example usage
        Permutations solution = new Permutations();
        int[] nums = { 1, 2, 3 };
        List<List<Integer>> result = solution.permute(nums);
        System.out.println(result);
    }
}