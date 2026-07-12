class Rectangle {

    // Method to calculate the area of a rectangle
    public int calculateArea(int length, int width) {
        return length * width;
    }
}

public class Main {
    public static void main(String[] args) {
        Rectangle rect = new Rectangle();

        int length = 8;
        int width = 5;

        int area = rect.calculateArea(length, width);

        System.out.println("Length: " + length);
        System.out.println("Width: " + width);
        System.out.println("Area of Rectangle: " + area);
    }
}
