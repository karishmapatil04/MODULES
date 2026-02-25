import java.util.Scanner;

public class sum_tilln {

public static void main(String[] args) {
    Scanner scn = new Scanner(System.in);
    int n = scn.nextInt();
    int sum = 0;
    for(int i=1; i<=n; i++){
        sum += i;
    }
    System.out.println("Sum till "+n+" is "+sum+".");
    scn.close();
}
}
