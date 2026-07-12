import java.util.*;

public class UniquePermutation {

    // Set to store the unique permutations
    Set<List<Integer>> ans = new HashSet<>();

    // Method to generate unique permutations of an array
    public List<List<Integer>> permuteUnique(int[] nums) {
        // Call helper function with initial index and empty list
        helper(0, nums, new ArrayList<Integer>());
        // Convert the set of permutations to a list of lists
        List<List<Integer>> listOfLists = new ArrayList<>(ans);
        return listOfLists;
    }

    // Helper method to generate unique permutations using backtracking
    public void helper(int idx, int[] nums, ArrayList<Integer> curr) {
        // If the current list has the same length as the input array, add it to the
        // result
        if (curr.size() == nums.length) {
            ans.add(new ArrayList<Integer>(curr));
            return;
        }

        // Iterate through the array starting from index 'idx'
        for (int i = idx; i < nums.length; i++) {
            // Skip duplicates to avoid repeating the same permutation
            if (i > idx && nums[i] == nums[i - 1])
                continue;

            // Add the current element to the permutation
            curr.add(nums[i]);
            // Swap the current element with the one at index 'idx'
            swap(nums, i, idx);
            // Recurse to generate the next part of the permutation
            helper(idx + 1, nums, curr);
            // Backtrack: undo the swap and remove the last added element
            swap(nums, i, idx);
            curr.remove(curr.size() - 1);
        }
    }

    // Swap method to swap elements in the array
    public void swap(int[] nums, int i, int idx) {
        int temp = nums[i];
        nums[i] = nums[idx];
        nums[idx] = temp;
    }

    public static void main(String[] args) {
        // Example usage
        UniquePermutation solution = new UniquePermutation();
        int[] nums = { 1, 1, 2 };
        List<List<Integer>> result = solution.permuteUnique(nums);
        System.out.println(result);
    }
}