package p_2908;

import java.util.Scanner;

/**
 * 문제
 * 상근이의 동생 상수는 수학을 정말 못한다. 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.
 * <p>
 * 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
 * <p>
 * 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.
 * <p>
 * 입력
 * 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.
 * <p>
 * 출력
 * 첫째 줄에 상수의 대답을 출력한다.
 */
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] inputs = sc.nextLine().split(" ");
        String a = inputs[0];
        String b = inputs[1];

        int numA = switchNum(a);
        int numB = switchNum(b);
        System.out.println(Math.max(numA, numB));
    }

    private static int switchNum(String num) {
        char[] chars = num.toCharArray();
        char tmp = chars[0];
        chars[0] = chars[2];
        chars[2] = tmp;
        String newNum = new String(chars);
        return Integer.parseInt(newNum);
    }
}
