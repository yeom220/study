package p_24313;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a1 = sc.nextInt();
        int a0 = sc.nextInt();
        int c = sc.nextInt();
        int n0 = sc.nextInt();
        int n1 = n0 + 1;

        int fn0 = (c - a1) * n0 - a0;
        int fn1 = (c - a1) * n1 - a0;

        if (fn0 < 0) {
            System.out.println(0);
        } else if (fn1 >= fn0) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}
