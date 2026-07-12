public class Circle {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    public double area() {
        return Math.PI * radius * radius;
    }

    public double circumference() {
        return 2 * Math.PI * radius;
    }
}

public class Main {
    public static void main(String[] args) {
        Circle circle = new Circle(5.0);

        System.out.println("radius: " + circle.getRadius());
        System.out.println("area: " + circle.area());
        System.out.println("circumference: " + circle.circumference());
    }
}