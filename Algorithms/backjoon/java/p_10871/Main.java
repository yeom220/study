package p_10871;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        int[] result = new int[N];
        for (int i = 0; i < N; i++) {
            if (X > arr[i])
                result[i] = arr[i];
        }
        for (int i : result) {
            if (i > 0)
                System.out.print(i + " ");
        }
    }
}
