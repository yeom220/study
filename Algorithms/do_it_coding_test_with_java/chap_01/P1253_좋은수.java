package chap_01;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 *
 */
public class P1253_좋은수 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        StringTokenizer stringTokenizer = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(stringTokenizer.nextToken());
        }
        Arrays.sort(A);
        int count = 0;
        for (int k = 0; k < N; k++) {
            int find = A[k];
            int i = 0;
            int j = N - 1;
            while (i < j) {
                if (A[i] + A[j] == find) {
                    if (i != k && j != k) {
                        count++;
                        break;
                    } else if (i == k) i++;
                    else j--;
                } else if (A[i] + A[j] < find) i++;
                else j--;
            }
        }
        System.out.println(count);
        br.close();
    }
}
