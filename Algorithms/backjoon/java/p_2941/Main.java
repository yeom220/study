package p_2941;

import java.util.Scanner;

/**
 * 문제
 * 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
 * <p>
 * 크로아티아 알파벳	변경
 * č	c=
 * ć	c-
 * dž	dz=
 * đ	d-
 * lj	lj
 * nj	nj
 * š	s=
 * ž	z=
 * 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
 * <p>
 * dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.
 * <p>
 * 입력
 * 첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-', '='로만 이루어져 있다.
 * <p>
 * 단어는 크로아티아 알파벳으로 이루어져 있다. 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
 * <p>
 * 출력
 * 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
 */
public class Main {
    public static void main(String[] args) {

        String[] c_alphabet = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        String input = new Scanner(System.in).next();
        int c_count = 0;
        int dz_count = 0;

        for (String s : c_alphabet) {
            int index = 0;
            while (true) {
                index = input.indexOf(s, index);
                if (index == -1) break;
                c_count += (s.length() - 1);
                if (s.equals("dz=")) {
                    dz_count++;
                }
                index++;
            }
        }

        System.out.println(input.length() - c_count + dz_count);
    }
}
