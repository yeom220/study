package p_1753;
import java.util.*;
import java.io.*;

public class Main {
    public static int V, E, K;
    public static int[] distance;
    public static boolean[] visited;
    public static List<Edge>[] list;
    public static PriorityQueue<Edge> pq = new PriorityQueue<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int V = Integer.parseInt(st.nextToken());
        int E = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(br.readLine());
        distance = new int[V + 1];
        visited = new boolean[V + 1];
        list = new ArrayList[V + 1];
        
    }

    static class Edge implements Comparable<Edge>{
        int node;
        int value;
        Edge(int node, int value){
            this.node = node;
            this.value = value;
        }
        public int compareTo(Edge e){
            if(this.value > e.value){
                return 1;
            }else {
                return -1;
            }
        }
    }
}
