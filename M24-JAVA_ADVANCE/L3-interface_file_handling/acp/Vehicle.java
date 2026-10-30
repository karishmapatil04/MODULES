import java.util.Scanner;

public class Vehicle {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int gear;
        int speed = 0;
        String brake;

        System.out.println("Enter current gear (1-5): ");
        gear = sc.nextInt();

        System.out.println("Are brakes applied? (yes/no): ");
        brake = sc.next();

        if (brake.equalsIgnoreCase("yes")) {
            speed = 0;
        } else {
            switch (gear) {
                case 1:
                    speed = 20;
                    break;

                case 2:
                    speed = 40;
                    break;

                case 3:
                    speed = 60;
                    break;

                case 4:
                    speed = 80;
                    break;

                case 5:
                    speed = 100;
                    break;

                default:
                    System.out.println("Invalid gear!");
                    return;
            }
        }

        System.out.println("Vehicle Speed: " + speed + " km/h");

        sc.close();
    }
}
