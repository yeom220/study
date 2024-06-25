package p_10986;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        long[] S = new long[N];
        long[] C = new long[M];
        long answer = 0;
        st = new StringTokenizer(br.readLine());
        S[0] = Long.parseLong(st.nextToken());
        // 수열 합 배열 만들기
        for (int i = 1; i < N; i++) {
            S[i] = S[i - 1] + Long.parseLong(st.nextToken());
        }
        for (int i = 0; i < N; i++) {
            // 합 배열의 모든 값에 % 연산 수행
            int remainder = (int) (S[i] % M);
            // 0 ~ i까지의 구간 합 자체가 0일 때 정답 더하기
            if (remainder == 0) answer++;
            // 나머지가 같은 인덱스의 개수 카운팅하기
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
