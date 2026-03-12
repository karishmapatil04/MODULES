class Personinfo {
    private String name;
    private int age;

    public Personinfo(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

class Studinfo extends Personinfo {
    private String major;

    public Studinfo(String name, int age, String major) {
        super(name, age); // Calls Person's constructor
        this.major = major;
    }

    public String getMajor() {
        return major;
    }
}

public class cons_subclass {
    public static void main(String[] args) {
        Studinfo student = new Studinfo("Alice", 20, "Computer Science");
        System.out.println("Name: " + student.getName());
        System.out.println("Age: " + student.getAge());
        System.out.println("Major: " + student.getMajor());
    }
}