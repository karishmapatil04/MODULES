import java.util.Scanner;

class acp_rotate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();

        int last = n % 10;
        int rem = n / 10;

        int count = 0, temp = rem;
        while (temp > 0) {
            temp /= 10;
            count++;
        }

        int result = last;
        for (int i = 0; i < count; i++)
            result *= 10;

        result += rem;

        System.out.println(result);
        sc.close();
    }
}

