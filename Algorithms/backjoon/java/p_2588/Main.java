/**
 * 문제
 * (세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
 * <p>
 * <p>
 * <p>
 * (1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
 * <p>
 * 입력
 * 첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
 * <p>
 * 출력
 * 첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
 */
package p_2588;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        String b = sc.nextLine();
        int numA = Integer.parseInt(a);
        int numB = Integer.parseInt(b);
        int[] nums = new int[3];
        int c = numA * numB;
        int idx = 0;
        for (String s : b.split("")) {
            nums[idx] = Integer.parseInt(s) * numA;
            idx++;
        }
        for (int i = nums.length-1; i >= 0; i--) {
            System.out.println(nums[i]);
        }
        System.out.println(c);
    }
}
