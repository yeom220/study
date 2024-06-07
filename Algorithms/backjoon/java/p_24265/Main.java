package p_24265;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        long cnt = 0;
        for(int i = 1; i < n; i++) {
            cnt += i;
        }
        System.out.println(cnt);
        System.out.println(2);
    }
}
