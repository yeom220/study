package p_2292;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int result = 1;
        int ranges = 1;

        while (ranges < n) {
            ranges += (6 * result++);
        }
        System.out.println(result);
    }
}
