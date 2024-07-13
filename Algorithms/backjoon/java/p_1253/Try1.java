package p_1253;

import java.util.Arrays;
import java.util.Scanner;

public class Try1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLong();
        }
        Arrays.sort(arr);
        int count = 0;
        for (int i = 0; i < n; i++) {
            long find = arr[i];
            int p1 = 0;
            int p2 = arr.length - 1;
            while (p1 < p2) {
                if (arr[p1] + arr[p2] == find) {
                    if (p1 == i) {
                        p1++;
                    } else if (p2 == i) {
                        p2--;
                    } else {
                        count++;
                        break;
                    }
                } else if (arr[p1] + arr[p2] > find) {
                    p2--;
                } else {
                    p1++;
                }
            }
        }
        System.out.println(count);
        sc.close();
    }
}
