package p_2745;

import java.util.Scanner;

/**
 * 문제
 * B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
 * <p>
 * 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
 * <p>
 * A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
 * <p>
 * 입력
 * 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
 * <p>
 * B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.
 * <p>
 * 출력
 * 첫째 줄에 B진법 수 N을 10진법으로 출력한다.
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        int b = sc.nextInt();

        long result = 0L;
        char[] chars = input.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            long num = 0L;
            char currentChar = chars[i];
            if (Character.isDigit(currentChar)) {
                num = Long.parseLong(String.valueOf(currentChar));
            } else {
                num = currentChar - 55;
            }

            long d = degree(b, chars.length - (i + 1));
            result += num * d;
        }
        System.out.println(result);
    }

    private static long degree(int a, int b) {
        long result = 1L;
        for (int i = 0; i < b; i++) {
            result *= a;
        }
        return result;
    }
}
