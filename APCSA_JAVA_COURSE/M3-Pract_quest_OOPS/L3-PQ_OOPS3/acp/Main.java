class Calculator {

    // Method to add two numbers
    public int addNumbers(int num1, int num2) {
        return num1 + num2;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();

        int result = calc.addNumbers(15, 25);

        System.out.println("Sum = " + result);
    }
}
