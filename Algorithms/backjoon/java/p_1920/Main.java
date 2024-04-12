package p_1920;

import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            boolean find = false;
            int target = Integer.parseInt(st.nextToken());
            int start = 0;
            int end = M - 1;
            while (start <= end){
                int mid_i = (start + end) / 2;
                int mid_v = A[mid_i];
                if(mid_v > target){
                    end = mid_i - 1;
                }
                else if(mid_v < target){
                    start = mid_i + 1;
                }
                else {
                    find = true;
                    break;
                }
            }
            if(find)
                bw.write("1 \n");
            else
                bw.write("0 \n");
        }
        bw.flush();
        bw.close();
    }
}
