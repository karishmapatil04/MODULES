import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    // Recursive method to find combinations
    public static void findCombinations(int[] candidates, int target, int index,
            ArrayList<Integer> current,
            ArrayList<ArrayList<Integer>> result) {

        // Base case
        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        if (target < 0 || index == candidates.length) {
            return;
        }

        // Include the current element
        current.add(candidates[index]);
        findCombinations(candidates, target - candidates[index], index, current, result);

        // Backtrack
        current.remove(current.size() - 1);

        // Exclude the current element and move to the next
        findCombinations(candidates, target, index + 1, current, result);
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Input number of candidates
        int n = sc.nextInt();

        int[] candidates = new int[n];

        // Input candidate values
        for (int i = 0; i < n; i++) {
            candidates[i] = sc.nextInt();
        }

        // Input target
        int target = sc.nextInt();

        ArrayList<ArrayList<Integer>> result = new ArrayList<>();

        findCombinations(candidates, target, 0, new ArrayList<>(), result);

        // Display the result
        System.out.println(result);

        sc.close();
    }
}