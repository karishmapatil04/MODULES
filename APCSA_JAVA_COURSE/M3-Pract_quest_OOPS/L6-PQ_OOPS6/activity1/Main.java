import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

// Base abstract class
abstract class Item {
    private String id;
    private String title;
    private LocalDate publicationDate;
    private int maxCheckoutDays;

    public Item(String id, String title, LocalDate publicationDate, int maxCheckoutDays) {
        this.id = id;
        this.title = title;
        this.publicationDate = publicationDate;
        this.maxCheckoutDays = maxCheckoutDays;
    }

    // Getters
    public String getId() {
        return id;
    }

    public String getTitle() {
        return title;
    }

    public LocalDate getPublicationDate() {
        return publicationDate;
    }

    public int getMaxCheckoutDays() {
        return maxCheckoutDays;
    }
}

class Book extends Item {
    private String author;
    private int pages;

    public Book(String id, String title, LocalDate publicationDate, String author, int pages) {
        super(id, title, publicationDate, 21); // Books: 21-day checkout
        this.author = author;
        this.pages = pages;
    }

    public String getAuthor() {
        return author;
    }

    public int getPages() {
        return pages;
    }
}

class CD extends Item {
    private String artist;
    private int tracks;

    public CD(String id, String title, LocalDate publicationDate, String artist, int tracks) {
        super(id, title, publicationDate, 14); // CDs: 14-day checkout
        this.artist = artist;
        this.tracks = tracks;
    }

    public String getArtist() {
        return artist;
    }

    public int getTracks() {
        return tracks;
    }
}

class DVD extends Item {
    private String director;
    private int runningTime;

    public DVD(String id, String title, LocalDate publicationDate, String director, int runningTime) {
        super(id, title, publicationDate, 7); // DVDs: 7-day checkout
        this.director = director;
        this.runningTime = runningTime;
    }

    public String getDirector() {
        return director;
    }

    public int getRunningTime() {
        return runningTime;
    }
}

class Patron {
    private String name;
    private int id;
    private List<Item> checkedOutItems;

    public Patron(String name, int id) {
        this.name = name;
        this.id = id;
        this.checkedOutItems = new ArrayList<>();
    }

    // Check out an item if under limit (max 10)
    public void checkOutItem(Item item) {
        if (checkedOutItems.size() < 10) {
            checkedOutItems.add(item);
        }
    }

    // Return an item
    public void returnItem(Item item) {
        checkedOutItems.remove(item);
    }

    // Get number of checked-out items
    public int getNumItemsCheckedOut() {
        return checkedOutItems.size();
    }

    // Getters
    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public List<Item> getCheckedOutItems() {
        return checkedOutItems;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create items
        Book book = new Book("B001", "1984", LocalDate.of(1949, 6, 8), "George Orwell", 328);
        DVD dvd = new DVD("D001", "Inception", LocalDate.of(2010, 7, 16), "Christopher Nolan", 148);
        CD cd = new CD("C001", "Thriller", LocalDate.of(1982, 11, 30), "Michael Jackson", 9);

        // Create patron Alice
        Patron alice = new Patron("Alice", 1234);
        alice.checkOutItem(book);
        alice.checkOutItem(dvd);
        System.out.println("Alice's checked-out items: " + alice.getNumItemsCheckedOut()); // 2

        // Return an item
        alice.returnItem(dvd);
        System.out.println("Alice's items after return: " + alice.getNumItemsCheckedOut()); // 1

        // Just to show CD exists
        alice.checkOutItem(cd);
        System.out.println("Alice's items after checking out a CD: " + alice.getNumItemsCheckedOut()); // 2
    }
}
