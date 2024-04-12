package p_1260;

import java.io.*;
import java.util.*;

public class Main {
    static boolean[] visited;
    static List<Integer>[] list;
//    static Queue<Integer> q = new LinkedList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int V = Integer.parseInt(st.nextToken());
        list = new List[N + 1];
        visited = new boolean[N + 1];

        for (int i = 1; i <= N; i++) {
            list[i] = new ArrayList<>();
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            list[s].add(e);
            list[e].add(s);
        }
        for (int i = 1; i <= N; i++) {
            Collections.sort(list[i]);
        }
        DFS(V);
        System.out.println();
        visited = new boolean[N + 1];
        BFS(V);
    }

    static void DFS(int node) {
//        if (visited[node]) return;
        visited[node] = true;
        System.out.print(node + " ");
        for (int i : list[node]) {
            if (!visited[i]) {
                DFS(i);
            }
        }
    }

    static void BFS(int node) {
        Queue<Integer> q = new LinkedList<>();
        visited[node] = true;
        q.add(node);

        while (!q.isEmpty()) {
            int i = q.poll();
            System.out.print(i + " ");
            for (int n : list[i]) {
                if (!visited[n]) {
                    visited[n] = true;
                    q.add(n);
                }
            }
        }
    }
}
