package p_1546;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int max = 0;
        int sum = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            int tmp = Integer.parseInt(st.nextToken());
            if (tmp > max)
                max = tmp;
            sum += tmp;
        }
        System.out.printf("%.2f", ((double) sum / max) * 100 / n);
    }
}
