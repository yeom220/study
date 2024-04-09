package chap_06;

import java.util.PriorityQueue;
import java.util.Scanner;

public class P1197_최소신장트리 {
    static int[] parent;
    static PriorityQueue<PEdge> queue;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();   // 노드 수
        int M = sc.nextInt();   // 에지 수
        queue = new PriorityQueue<>();  // 자동 정렬을 위해 우선순위 큐 자료구조 선택
        parent = new int[N + 1];
        // TODO:
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }
        for (int i = 0; i < M; i++) {
            int s = sc.nextInt();
            int e = sc.nextInt();
            int v = sc.nextInt();
            queue.add(new PEdge(s, e, v));
        }
        int useEdge = 0;
        int result = 0;
        while (useEdge < N - 1) {
            PEdge now = queue.poll();
            if (find(now.s) != find(now.e)) {   // 같은 부모(대표노드)가 아니라면 연결해도 사이클이 생기지 않음
                union(now.s, now.e);
                result = result + now.v;
                useEdge++;
            }
        }
        System.out.println(result);
    }

    private static void union(int a, int b) {    // union 연산: 대표 노드끼리 연결
        a = find(a);
        b = find(b);
        if (a != b) {
            parent[b] = a;
        }
    }

    private static int find(int a) { // find 연산
        if (a == parent[a])
            return a;
        else
            return parent[a] = find(parent[a]); // 재귀 함수의 형태로 구현 -> 경로 압축 부분
    }
}

class PEdge implements Comparable<PEdge> {
    int s;
    int e;
    int v;

    public PEdge(int s, int e, int v) {
        this.s = s;
        this.e = e;
        this.v = v;
    }

    @Override
    public int compareTo(PEdge o) {
        // 가중치를 기준으로 오름차순 정렬을 하기 위해 compareTo 재정의
        return this.v - o.v;
    }
}
