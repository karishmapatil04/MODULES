public class Main {

    // Recursive method to generate permutations
    public static void generatePermutations(String prefix, String remaining, int[] count, int k) {
        if (remaining.length() == 0) {
            count[0]++;
            if (count[0] == k) {
                System.out.println("K-th Permutation: " + prefix);
            }
            return;
        }

        for (int i = 0; i < remaining.length(); i++) {
            generatePermutations(
                    prefix + remaining.charAt(i),
                    remaining.substring(0, i) + remaining.substring(i + 1),
                    count,
                    k);
        }
    }

    public static void main(String[] args) {
        int n = 3;
        int k = 4;

        // Create the string "123...n"
        String numbers = "";
        for (int i = 1; i <= n; i++) {
            numbers += i;
        }

        int[] count = { 0 }; // Used to keep track of permutation count

        generatePermutations("", numbers, count, k);
    }
}