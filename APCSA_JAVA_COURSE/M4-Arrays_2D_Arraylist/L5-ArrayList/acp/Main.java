import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        // Create an ArrayList
        ArrayList<String> fruits = new ArrayList<>();

        // Add elements
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Mango");
        fruits.add("Orange");

        // Display the ArrayList
        System.out.println("ArrayList: " + fruits);

        // Access an element
        System.out.println("First Fruit: " + fruits.get(0));

        // Remove an element
        fruits.remove("Banana");

        // Display updated ArrayList
        System.out.println("After Removing Banana: " + fruits);

        // Display the size of the ArrayList
        System.out.println("Number of Fruits: " + fruits.size());

        // Traverse the ArrayList
        System.out.println("Fruits List:");
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}