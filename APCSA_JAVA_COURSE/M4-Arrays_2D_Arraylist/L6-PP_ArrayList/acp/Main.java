import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        // Create an ArrayList
        ArrayList<Integer> numbers = new ArrayList<>();

        // Add elements
        numbers.add(10);
        numbers.add(20);
        numbers.add(30);
        numbers.add(40);
        numbers.add(50);

        System.out.println("Original ArrayList: " + numbers);

        // Swap the first and last elements
        int first = numbers.get(0);
        int lastIndex = numbers.size() - 1;

        numbers.set(0, numbers.get(lastIndex));
        numbers.set(lastIndex, first);

        System.out.println("ArrayList after swapping first and last elements: " + numbers);
    }
}
