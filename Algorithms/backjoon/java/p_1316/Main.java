package p_1316;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * 문제
 * 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
 * <p>
 * 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
 * <p>
 * 입력
 * 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.
 * <p>
 * 출력
 * 첫째 줄에 그룹 단어의 개수를 출력한다.
 */

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;

        for (int i = 0; i < n; i++) {
            List<Character> checked = new ArrayList<>();
            char prev = ' ';
            boolean isGroup = true;
            String s = sc.next();
            for (char c : s.toCharArray()) {
                if (prev != c && !checked.contains(c)) {
                    checked.add(c);
                    prev = c;
                } else if (prev == c) {
                    continue;
                } else {
                    isGroup = false;
                    break;
                }
            }
            if (isGroup) {
                count++;
            }
        }

        System.out.println(count);
    }
}
