import java.util.Scanner;

class Hello_user {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        String str = scn.nextLine();
        System.out.println("The String is "+str);
        int num = scn.nextInt();
        System.out.println("Number is "+num);
        float fnum = scn.nextFloat();
        System.out.println("The floating num is "+fnum);
        scn.close();
    }
}