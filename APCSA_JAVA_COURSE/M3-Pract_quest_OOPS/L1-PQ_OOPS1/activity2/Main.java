package activity2;

public class Main {
    public static void main(String[] args) {
        // Create and test objects
        Student student = new Student("John Doe", 28, "Computer Science");
        Book book = new Book("The Hobbit", "J.R.R. Tolkien", 295);

        // Print values from the object
        System.out.println(student.getName());
        System.out.println(student.getAge());
        System.out.println(student.getMajor());

        // Print values from the object using method reference
        System.out.println("Book's Information:");
        System.out.println("Name: " + book.getTitle());
        System.out.println("Author: " + book.getAuthor());
        System.out.println("Pages: " + book.getNumPages());
    }
}
