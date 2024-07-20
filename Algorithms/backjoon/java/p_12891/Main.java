package p_12891;

import java.util.Scanner;

public class Main {
    static int[] checkArr = new int[4];
    static int[] myArr = new int[4];
    static int checkSecret = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int S = sc.nextInt();
        int P = sc.nextInt();
        String A = sc.next();
        int result = 0;
        for (int i = 0; i < 4; i++) {
            checkArr[i] = sc.nextInt();
            if (checkArr[i] == 0) checkSecret++;
        }
        for (int i = 0; i < P; i++) {
            char c = A.charAt(i);
            add(c);
        }
        if (checkSecret == 4) {
            result++;
        }

        for (int i = P; i < S; i++) {
            char addChar = A.charAt(i);
            char removeChar = A.charAt(i - P);
            add(addChar);
            remove(removeChar);
            if (checkSecret == 4) {
                result++;
            }
        }
        System.out.println(result);
    }

    public static void add(char c) {
        if (c == 'A') {
            myArr[0]++;
            if (myArr[0] == checkArr[0]) {
                checkSecret++;
            }
        } else if (c == 'C') {
            myArr[1]++;
            if (myArr[1] == checkArr[1]) {
                checkSecret++;
            }
        } else if (c == 'G') {
            myArr[2]++;
            if (myArr[2] == checkArr[2]) {
                checkSecret++;
            }
        } else if (c == 'T') {
            myArr[3]++;
            if (myArr[3] == checkArr[3]) {
                checkSecret++;
            }
        }
    }

    public static void remove(char c) {
        if (c == 'A') {
            if (myArr[0] == checkArr[0]) {
                checkSecret--;
            }
            myArr[0]--;
        } else if (c == 'C') {
            if (myArr[1] == checkArr[1]) {
                checkSecret--;
            }
            myArr[1]--;
        } else if (c == 'G') {
            if (myArr[2] == checkArr[2]) {
                checkSecret--;
            }
            myArr[2]--;
        } else if (c == 'T') {
            if (myArr[3] == checkArr[3]) {
                checkSecret--;
            }
            myArr[3]--;
        }
    }
}
