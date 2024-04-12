package p_1717;

import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int[] A;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        A = new int[N + 1];

        for (int i = 1; i <= N; i++) {
            A[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int type = Integer.parseInt(st.nextToken());
            int node1 = Integer.parseInt(st.nextToken());
            int node2 = Integer.parseInt(st.nextToken());
            if (type == 0) {
                union(node1, node2);
            } else {
                if (find(node1) == find(node2)) {
                    bw.write("YES \n");
                } else {
                    bw.write("NO \n");
                }
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }

    static void union(int n1, int n2) {
        if (n2 > n1) {
            int tmp = n1;
            n1 = n2;
            n2 = tmp;
        }
        n1 = find(n1);
        n2 = find(n2);
        if (n1 != n2) {
            A[n2] = n1;
        }
    }

    static int find(int n) {
        if (A[n] == n) {
            return n;
        }
        return A[n] = find(A[n]);
    }
}
