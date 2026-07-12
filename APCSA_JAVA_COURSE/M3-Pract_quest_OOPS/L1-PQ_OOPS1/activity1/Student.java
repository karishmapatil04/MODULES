package activity1;

public class Student extends Person {
    private String major;

    public Student(String name, int age, String major) {
    super(name, age); // Calls Person's constructor
    this.major = major;
    }

    public String getMajor() {
    return major;
    }
}
