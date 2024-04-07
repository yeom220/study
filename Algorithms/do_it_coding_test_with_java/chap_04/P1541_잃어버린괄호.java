package chap_04;

import java.util.Scanner;

public class P1541_잃어버린괄호 {
    static int answer = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String example = sc.nextLine();
        String[] str = example.split("-");
        for (int i = 0; i < str.length; i++) {
            int temp = mySum(str[i]);
            if (i == 0) {
                answer = answer + temp;
            } else {
                answer -= temp;
            }
        }
        System.out.println(answer);
    }

    private static int mySum(String str) {
        String[] temp = str.split("[+]");
        int sum = 0;
        for (String s : temp) {
            sum += Integer.parseInt(s);
        }
        return sum;
    }
}
