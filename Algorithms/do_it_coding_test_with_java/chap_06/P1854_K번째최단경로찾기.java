package chap_06;
/**
 * 문제
 * 봄캠프를 마친 김진영 조교는 여러 도시를 돌며 여행을 다닐 계획이다. 그런데 김 조교는, '느림의 미학'을 중요시하는 사람이라 항상 최단경로로만 이동하는 것은 별로 좋아하지 않는다. 하지만 너무 시간이 오래 걸리는 경로도 그리 매력적인 것만은 아니어서, 적당한 타협안인 '
 * $k$번째 최단경로'를 구하길 원한다. 그를 돕기 위한 프로그램을 작성해 보자.
 * <p>
 * 입력
 * 첫째 줄에
 * $n$,
 * $m$,
 * $k$가 주어진다. (
 * $1 ≤ n ≤ 1\,000$,
 * $0 ≤ m ≤ 250\,000$,
 * $1 ≤ k ≤ 100$,
 * $mk ≤ 3\,000\,000$)
 * $n$과
 * $m$은 각각 김 조교가 여행을 고려하고 있는 도시들의 개수와, 도시 간에 존재하는 도로의 수이다.
 * <p>
 * 이어지는
 * $m$개의 줄에는 각각 도로의 정보를 제공하는 세 개의 정수
 * $a$,
 * $b$,
 * $c$가 포함되어 있다. 이것은
 * $a$번 도시에서
 * $b$번 도시로 갈 때는
 * $c$의 시간이 걸린다는 의미이다. (
 * $1 ≤ a, b ≤ n$,
 * $1 ≤ c ≤ 1\,000$)
 * <p>
 * 도시의 번호는
 * $1$번부터
 * $n$번까지 연속하여 붙어 있으며,
 * $1$번 도시는 시작도시이다. 두 도로의 시작점과 도착점이 모두 같은 경우는 없다.
 * <p>
 * 출력
 * <p>
 * $n$개의 줄을 출력한다.
 * $i$번째 줄에
 * $1$번 도시에서
 * $i$번 도시로 가는
 * $k$번째 최단경로의 소요시간을 출력한다.
 * <p>
 * 경로의 소요시간은 경로 위에 있는 도로들을 따라 이동하는데 필요한 시간들의 합이다.
 * $i$번 도시에서
 * $i$번 도시로 가는 최단경로는
 * $0$이지만, 일반적인
 * $k$번째 최단경로는
 * $0$이 아닐 수 있음에 유의한다. 또,
 * $k$번째 최단경로가 존재하지 않으면
 * $-1$을 출력한다. 최단경로에 같은 정점이 여러 번 포함되어도 된다.
 */

import java.io.*;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class P1854_K번째최단경로찾기 {
    static final int INF = 100000000;

    public static void main(String[] args) throws IOException {
        int N, M, K;
        int[][] W = new int[1001][1001];
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        PriorityQueue<Integer>[] distQueue = new PriorityQueue[N + 1];
        Comparator<Integer> cp = new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {    // 오름차순 정렬
                return o1 < o2 ? 1 : -1;
            }
        };
        for (int i = 0; i <= N; i++) {
            distQueue[i] = new PriorityQueue<>(K, cp);
        }
        for (int i = 0; i < M; i++) {   // 인접 행렬에 그래프 데이터 저장
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            W[a][b] = c;
        }
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(1, 0));
        distQueue[1].add(0);
        while (!pq.isEmpty()) {
            Node u = pq.poll();
            for (int adjNode = 1; adjNode <= N; adjNode++) {
                // 연결된 모든 노드로 검색하기(시간 복잡도 측면에서 인접 행렬이 불리한 이유)
                if (W[u.node][adjNode] != 0) {
                    // 저장된 경로가 K개가 안 될때는 그냥 추가
                    if (distQueue[adjNode].size() < K) {
                        distQueue[adjNode].add(u.cost + W[u.node][adjNode]);
                        pq.add(new Node(adjNode, u.cost + W[u.node][adjNode]));
                    }
                    // 저장된 경로가 K개이고, 현재 가장 큰 값보다 작을 때만 추가
                    else if (distQueue[adjNode].peek() > u.cost + W[u.node][adjNode]) {
                        distQueue[adjNode].poll();  // 기존 큐에서 Max값 먼저 삭제해야 함
                        distQueue[adjNode].add(u.cost + W[u.node][adjNode]);
                        pq.add(new Node(adjNode, u.cost + W[u.node][adjNode]));
                    }
                }
            }
        }
        for (int i = 1; i <= N; i++) {  // K번째 경로 출력
            if (distQueue[i].size() == K) {
                bw.write(distQueue[i].peek() + "\n");
            } else {
                bw.write(-1 + "\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}

// 노드 클래스 작성
class Node implements Comparable<Node> {
    int node;
    int cost;

    public Node(int node, int cost) {
        this.node = node;
        this.cost = cost;
    }

    @Override
    public int compareTo(Node o) {
        return this.cost < o.cost ? -1 : 1;
    }
}
