package p_11724;
/**
 * 문제
 * 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
 * <p>
 * 입력
 * 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
 * <p>
 * 출력
 * 첫째 줄에 연결 요소의 개수를 출력한다.
 */

import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] list;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int node = Integer.parseInt(st.nextToken());
        int edge = Integer.parseInt(st.nextToken());
        list = new List[node + 1];
        visited = new boolean[node + 1];
        int count = 0;

        for (int i = 1; i <= node; i++) {
            list[i] = new ArrayList<>();
        }
        for (int i = 0; i < edge; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            list[u].add(v);
            list[v].add(u);
        }

        for (int i = 1; i <= node; i++) {
            if (visited[i]) continue;
            DFS(i);
            count++;
        }
        System.out.println(count);
    }

    private static void DFS(int node) {
        if (visited[node]) return;
        visited[node] = true;
        for (int n : list[node]) {
            if (!visited[n])
                DFS(n);
        }
    }
}
