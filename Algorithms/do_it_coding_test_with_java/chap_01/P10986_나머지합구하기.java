package chap_01;

import java.util.Scanner;

/**
 * 문제
 * 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
 * <p>
 * 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.
 * <p>
 * 입력
 * 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 106, 2 ≤ M ≤ 103)
 * <p>
 * 둘째 줄에 N개의 수 A1, A2, ..., AN이 주어진다. (0 ≤ Ai ≤ 109)
 * <p>
 * 출력
 * 첫째 줄에 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 출력한다.
 */

public class P10986_나머지합구하기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        long[] S = new long[N];
        long[] C = new long[M];
        long answer = 0;
        S[0] = sc.nextInt();

        // 수열 합 배열 만들기
        for (int i = 1; i < N; i++) {
            S[i] = S[i - 1] + sc.nextInt();
        }

        // 합 배열의 모든 값에 % 연산 수행하기
        for (int i = 0; i < N; i++) {
            int remainder = (int) (S[i] % M);
            // 0 ~ i까지의 구간 합 자체가 0일 때 정답 더하기
            if (remainder == 0) answer++;
            // 나머지가 같은 인덱스의 개수 카운팅 하기
            C[remainder]++;
        }

        for (int i = 0; i < M; i++) {
            if (C[i] > 1) {
                // 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
                answer = answer + (C[i] * (C[i] - 1) / 2);
            }
        }
        System.out.println(answer);
    }
}
