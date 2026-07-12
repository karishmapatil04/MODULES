class Employee {
    // Instance variables
    int id;
    String name;
    double salary;

    // Method to assign values
    void setDetails(int empId, String empName, double empSalary) {
        id = empId;
        name = empName;
        salary = empSalary;
    }

    // Method to display employee details
    void displayDetails() {
        System.out.println("Employee ID: " + id);
        System.out.println("Employee Name: " + name);
        System.out.println("Employee Salary: " + salary);
    }
}

public class Main {
    public static void main(String[] args) {
        // Create an Employee object
        Employee emp = new Employee();

        // Set employee details
        emp.setDetails(101, "John", 50000);

        // Display employee details
        emp.displayDetails();
    }
}
