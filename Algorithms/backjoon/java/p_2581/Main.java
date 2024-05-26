package p_2581;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int[] arr = new int[10001];
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();

        for (int cur = m; cur <= n; cur++) {
            if (arr[cur] == 2) {
                continue;
            }
            int count = 0;
            int mul = 1;
            for (int j = 2; j < cur; j++) {
                if (cur % j == 0) {
                    count++;
                    break;
                }
            }
            if (count == 0) {
                arr[cur] = 1;
            } else {
                while (cur * mul < n) {
                    arr[cur * mul++] = 2;
                }
            }
        }
        int sum = 0;
        List<Integer> answers = new ArrayList<>();
        for (int i = m; i <= n; i++) {
            if (i == 1) {
                continue;
            }
            if (arr[i] == 1) {
                sum += i;
                answers.add(i);
            }
        }
        if (answers.size() > 0) {
            System.out.println(sum);
            System.out.println(answers.get(0));
        } else {
            System.out.println(-1);
        }
    }
}
