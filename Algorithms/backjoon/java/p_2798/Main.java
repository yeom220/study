package p_2798;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            nums.add(sc.nextInt());
        }
        nums.sort((a, b) -> a - b);
        int result = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (j == i) continue;
                for (int k = 0; k < N; k++) {
                    if (k == i || k == j) {
                        continue;
                    }
                    int sum = nums.get(i) + nums.get(j) + nums.get(k);
                    if (sum > M) {
                        break;
                    }
                    result = Math.max(result, sum);
                }
            }
        }
        System.out.println(result);
    }
}
