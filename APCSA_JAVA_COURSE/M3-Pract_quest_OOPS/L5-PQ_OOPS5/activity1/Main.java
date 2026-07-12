import java.util.ArrayList;

class Course {
    private String name;
    private int credits;
    private double grade;

    public Course(String name, int credits) {
        this.name = name;
        this.credits = credits;
        this.grade = 0.0;
    }

    public void setGrade(double grade) {
        this.grade = grade;
    }

    public double getGrade() {
        return grade;
    }

    public int getCredits() {
        return credits;
    }

    public String getName() {
        return name;
    }

    // Convert numerical grade to letter grade
    public String getLetterGrade() {
        if (grade >= 4.0)
            return "A";
        else if (grade >= 3.7)
            return "A-";
        else if (grade >= 3.3)
            return "B+";
        else if (grade >= 3.0)
            return "B";
        else if (grade >= 2.7)
            return "B-";
        else
            return "C";
    }
}

class Student {
    private String name;
    private int id;
    private ArrayList<Course> courses;

    public Student(String name, int id) {
        this.name = name;
        this.id = id;
        courses = new ArrayList<>();
    }

    public void addCourse(Course course) {
        courses.add(course);
    }

    public void removeCourse(Course course) {
        courses.remove(course);
    }

    public double getGPA() {
        if (courses.isEmpty())
            return 0.0;

        double total = 0;
        for (Course course : courses) {
            total += course.getGrade();
        }
        return total / courses.size();
    }

    public String getTranscript() {
        StringBuilder transcript = new StringBuilder();
        transcript.append("Name: ").append(name).append("\n");
        transcript.append("ID: ").append(id).append("\n");

        for (Course course : courses) {
            transcript.append("Course: ")
                    .append(course.getName())
                    .append(" (").append(course.getCredits()).append(" credits)\n")
                    .append("Grade: ")
                    .append(course.getGrade())
                    .append(" (").append(course.getLetterGrade()).append(")\n\n");
        }
        return transcript.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        // Alice
        Course cs = new Course("Computer Science", 4);
        cs.setGrade(3.7);

        Student alice = new Student("Alice", 1234);
        alice.addCourse(cs);
        System.out.println("Alice's Initial GPA: " + alice.getGPA());

        Course math = new Course("Math", 3);
        alice.addCourse(math);
        math.setGrade(4.0);
        System.out.println("Alice's Updated GPA: " + alice.getGPA());

        // Bob
        Course csBob = new Course("Computer Science", 4);
        csBob.setGrade(3.0);

        Course mathBob = new Course("Math", 3);
        mathBob.setGrade(3.5);

        Student bob = new Student("Bob", 5678);
        bob.addCourse(csBob);
        bob.addCourse(mathBob);

        System.out.println("\nBob's GPA: " + bob.getGPA());
        System.out.println("Bob's Transcript:\n" + bob.getTranscript());
    }
}
