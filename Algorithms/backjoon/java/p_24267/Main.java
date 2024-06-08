package p_24267;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        long count = 0;
        int mul = n - 2;
        for (long i = 1; i <= n - 2; i++) {
            count += (i * mul--);
        }
        System.out.println(count);
        System.out.println(3);
    }
}
