class NumberOperations {

    // Method to check if a number is even
    public boolean isEven(int number) {
        return number % 2 == 0;
    }
}

public class Main {
    public static void main(String[] args) {
        NumberOperations obj = new NumberOperations();

        int num = 12;

        if (obj.isEven(num)) {
            System.out.println(num + " is an even number.");
        } else {
            System.out.println(num + " is an odd number.");
        }
    }
}
