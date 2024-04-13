package p_1516;

import java.io.*;
import java.util.*;

public class Main {
    static int[] time;
    static List<Integer>[] list;
    static int[] indegree;
    static int[] answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        time = new int[N + 1];
        list = new List[N + 1];
        indegree = new int[N + 1];
        answer = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            list[i] = new ArrayList<>();
        }

        StringTokenizer st;
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            time[i] = Integer.parseInt(st.nextToken());
            while (st.hasMoreTokens()) {
                int node = Integer.parseInt(st.nextToken());
                if (node == -1) {
                    break;
                }
                list[node].add(i);
                indegree[i]++;
            }
        }

        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0){
                q.offer(i);
            }
        }
        while (!q.isEmpty()){
            int now = q.poll();
            for(int next : list[now]){
                indegree[next]--;
                answer[next] = Math.max(answer[next], answer[now] + time[now]);
                if (indegree[next] == 0){
                    q.offer(next);
                }
            }
        }
        for (int i = 1; i <= N; i++) {
            System.out.println(answer[i] + time[i]);
        }
    }
}