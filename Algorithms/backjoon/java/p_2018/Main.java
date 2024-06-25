package p_2018;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int answer = 1;
        int n = new Scanner(System.in).nextInt();
        int[] sumArr = new int[n];
        sumArr[0] = 1;
        for (int i = 1; i < n; i++) {
            sumArr[i] = sumArr[i - 1] + i;
        }
        int p1 = 0;
        int p2 = 1;
        while (p1 < p2 && p2 < n) {
            int sum = sumArr[p2] - sumArr[p1];
            if (sum > n) {
                p1++;
            } else if (sum < n) {
                p2++;
            } else {
                answer++;
                p1++;
            }
        }
        System.out.println(answer);
    }
}
