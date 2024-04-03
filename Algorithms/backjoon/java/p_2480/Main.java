package p_2480;
/**
 * 문제
 * 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
 * <p>
 * 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
 * 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
 * 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
 * 예를 들어, 3개의 눈 3, 3, 6이 주어지면 상금은 1,000+3×100으로 계산되어 1,300원을 받게 된다. 또 3개의 눈이 2, 2, 2로 주어지면 10,000+2×1,000 으로 계산되어 12,000원을 받게 된다. 3개의 눈이 6, 2, 5로 주어지면 그중 가장 큰 값이 6이므로 6×100으로 계산되어 600원을 상금으로 받게 된다.
 * <p>
 * 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.
 * <p>
 * 입력
 * 첫째 줄에 3개의 눈이 빈칸을 사이에 두고 각각 주어진다.
 * <p>
 * 출력
 * 첫째 줄에 게임의 상금을 출력 한다.
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int dice1 = scanner.nextInt();
        int dice2 = scanner.nextInt();
        int dice3 = scanner.nextInt();
        List<Integer> dices = new ArrayList<>();
        dices.add(dice1);
        dices.add(dice2);
        dices.add(dice3);
        dices.sort((a, b) -> a.compareTo(b));
        int max = 0;
        ArrayList<Integer> list = new ArrayList<>();
        for (int dice : dices) {
            if (dice > max) {
                max = dice;
                if (list.size() <= 1) {
                    list.clear();
                    list.add(dice);
                }
            } else if (dice == max) {
                list.add(dice);
            }
        }
        int count = list.size();
        int num = list.get(0);
        if (count == 3) {
            System.out.println(10000 + num * 1000);
        } else if (count == 2) {
            System.out.println(1000 + num * 100);
        } else {
            System.out.println(num * 100);
        }
    }
}