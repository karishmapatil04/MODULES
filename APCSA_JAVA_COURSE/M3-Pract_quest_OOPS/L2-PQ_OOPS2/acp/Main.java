class Student {
    // Instance variables
    String name;
    int age;

    // Method to assign values
    void setDetails(String n, int a) {
        name = n;
        age = a;
    }

    // Method to display values
    void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

public class Main {
    // Function (static method)
    public static void greet() {
        System.out.println("Welcome to Java Programming!");
    }

    public static void main(String[] args) {
        // Calling the function
        greet();

        // Creating an object
        Student s1 = new Student();

        // Calling instance methods
        s1.setDetails("Alice", 20);
        s1.displayDetails();
    }
}