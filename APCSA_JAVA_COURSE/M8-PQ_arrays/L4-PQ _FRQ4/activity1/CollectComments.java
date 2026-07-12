import java.util.ArrayList;
import java.util.Scanner;

class Review {
    private String comment;

    public Review(String comment) {
        this.comment = comment;
    }

    public String getComment() {
        return comment;
    }
}

public class CollectComments {

    // Method to collect comments that contain an exclamation mark and ensure proper
    // formatting
    public ArrayList<String> collectComments(ArrayList<Review> allReviews) {
        ArrayList<String> comments = new ArrayList<>();

        // Loop through all reviews
        for (int i = 0; i < allReviews.size(); i++) {
            String comment = allReviews.get(i).getComment();

            // If the comment contains an exclamation mark
            if (comment.contains("!")) {
                // Format the comment with its index
                String formattedComment = String.format("%d-%s", i, comment);

                // Ensure the comment ends with either a period or an exclamation mark
                if (!comment.endsWith("!") && !comment.endsWith(". ")) {
                    formattedComment += ".";
                }

                // Add the formatted comment to the list
                comments.add(formattedComment);
            }
        }

        return comments;
    }

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) { // Using try-with-resources
            CollectComments obj = new CollectComments();

            // Prompt the user to enter the number of reviews
            System.out.print("Enter the number of reviews: ");
            int n = sc.nextInt();
            sc.nextLine(); // Consume the leftover newline character

            // Create an ArrayList to store the reviews
            ArrayList<Review> allReviews = new ArrayList<>();

            // Prompt user to enter reviews
            for (int i = 0; i < n; i++) {
                System.out.print("Enter comment for review " + (i + 1) + ": ");
                String comment = sc.nextLine();
                allReviews.add(new Review(comment));
            }

            // Get and print the formatted comments
            ArrayList<String> comments = obj.collectComments(allReviews);
            System.out.println("Formatted comments:");
            for (String comment : comments) {
                System.out.println(comment);
            }
        }
    }
}