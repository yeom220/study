package p_1253;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * 문제
 * N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
 * <p>
 * N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
 * <p>
 * 수의 위치가 다르면 값이 같아도 다른 수이다.
 * <p>
 * 입력
 * 첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000), 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다. (|Ai| ≤ 1,000,000,000, Ai는 정수)
 * <p>
 * 출력
 * 좋은 수의 개수를 첫 번째 줄에 출력한다.
 */
public class Main {
    public static void main(String[] agrs) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        long[] A = new long[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Long.parseLong(st.nextToken());
        }
        Arrays.sort(A);

        int count = 0;
        for (int k = 0; k < N; k++) {
            int i = 0;
            int j = N - 1;
            long find = A[k];
            while (i < j) {
                long sum = A[i] + A[j];
                if (sum == find) {
                    if (i != k && j != k) {
                        count++;
                        break;
                    } else if (i == k) {
                        i++;
                    } else if (j == k) {
                        j--;
                    }
                } else if (sum < find) {
                    i++;
                } else if (sum > find) {
                    j--;
                }
            }
        }
        System.out.println(count);
        br.close();
    }
}
