package p_2903;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int a = (int) (Math.pow(2, n) + 1);
        System.out.println(a * a);
    }
}
