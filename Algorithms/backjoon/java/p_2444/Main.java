package p_2444;

import java.util.Scanner;

/**
 * 문제
 * 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
 * <p>
 * 입력
 * 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
 * <p>
 * 출력
 * 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
 */
public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        int count = 1;

        for (int i = 1; i < n * 2; i++) {
            int blank = Math.abs(n - i);
            int printed = 0;

            for (int j = 0; j < n * 2; j++) {
                if (blank > 0) {
                    System.out.print(" ");
                    blank--;
                } else if (count > printed) {
                    System.out.print("*");
                    printed++;
                } else {
                    break;
                }
            }
            if (n > i) {
                count += 2;
            } else {
                count -= 2;
            }
            System.out.println();
        }
    }
}
