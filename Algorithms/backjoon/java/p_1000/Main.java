package p_1000;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        /**
         * 문제.
         * 입력 받은 두 숫자를 더해 출력하라.
         */
        try (Scanner scanner = new Scanner(System.in)) {
            int a, b;
            a = scanner.nextInt();
            b = scanner.nextInt();

            System.out.println(a+b);
        }

    }
}
