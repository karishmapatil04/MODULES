package activity1;

public class Main {
    public static void main(String[] args) {
    Student student = new Student("Alice", 20, "Computer Science");
    System.out.println("Name: " + student.getName());
    System.out.println("Age: " + student.getAge());
    System.out.println("Major: " + student.getMajor());
    }
}