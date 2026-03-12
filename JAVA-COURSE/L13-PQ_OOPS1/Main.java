class Person13 {
    private String name;
    private int age;

    public Person13(String name, int age) {
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

class Studentinfo extends Person13 {
    private String major;

    public Studentinfo(String name, int age, String major) {
        super(name, age);
        this.major = major;
    }

    public String getMajor() {
        return major;
    }
}

class Bookname {
    private String title;
    private String author;
    private int numPages;

    public Bookname(String t, String a, int np) {
        title = t;
        author = a;
        numPages = np;
    }

    public String getTitle() {
        return title;
    }

    public String getAuthor() {
        return author;
    }

    public int getNumPages() {
        return numPages;
    }
}

public class Main {
    public static void main(String[] args) {

        Studentinfo student = new Studentinfo("John Doe", 28, "Computer Science");
        Bookname book = new Bookname("The Hobbit", "J.R.R. Tolkien", 295);

        System.out.println(student.getName());
        System.out.println(student.getAge());
        System.out.println(student.getMajor());

        System.out.println("Book's Information:");
        System.out.println("Name: " + book.getTitle());
        System.out.println("Author: " + book.getAuthor());
        System.out.println("Pages: " + book.getNumPages());
    }
}