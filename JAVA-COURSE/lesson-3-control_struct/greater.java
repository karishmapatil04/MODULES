import java.util.Scanner;

class greater {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int num = scn.nextInt();

        if (num > 10) {
            System.out.println("Yes I'm Greater");
        } else {
            System.out.println("Sorry I feel bad");
        }
        scn.close();
    }
}
