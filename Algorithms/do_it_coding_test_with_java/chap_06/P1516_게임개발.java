package chap_06;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class P1516_게임개발 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<ArrayList<Integer>> A = new ArrayList<>();

        for (int i = 0; i <= N; i++) {
            A.add(new ArrayList<>());
        }

        int[] indegree = new int[N + 1];    // 진입 차수 배열
        int[] selfBuild = new int[N + 1];   // 자기 자신을 짓는 데 걸리는 시간
        for (int i = 1; i <= N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            selfBuild[i] = Integer.parseInt(st.nextToken());    // 건물을 짓는 데 걸리는 시간
            while (true) {  // 인접 리스트 초기화
                int preTemp = Integer.parseInt(st.nextToken());
                if (preTemp == -1) break;
                A.get(preTemp).add(i);
                indegree[i]++;  // 진입 차수 배열 초기화
            }
        }
        // 위상 정렬
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }
        int[] result = new int[N + 1];
        while (!queue.isEmpty()) {
            int now = queue.poll();
            for (int next : A.get(now)) {
                indegree[next]--;
                // 시간 업데이트
                System.out.println(next+": "+result[next] +" "+result[now]+" "+selfBuild[now]);
                result[next] = Math.max(result[next], result[now] + selfBuild[now]);
                if (indegree[next] == 0) {
                    queue.offer(next);
                }
            }
        }
//        for (int i = 1; i <= N; i++) {
//            System.out.println(result[i] + selfBuild[i]);
//        }
    }

}
