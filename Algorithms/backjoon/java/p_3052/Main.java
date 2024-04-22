package p_3052;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int mod = 42;
        boolean[] checks = new boolean[1001];
        for (int i = 1; i <= 10; i++) {
            int n = sc.nextInt();
            int r = n % mod;
            if(!checks[r]) {
                checks[r] = true;
            }
        }
        int count = 0;
        for (boolean check : checks) {
            if (check) {
                count++;
            }
        }
        System.out.println(count);
    }
}
