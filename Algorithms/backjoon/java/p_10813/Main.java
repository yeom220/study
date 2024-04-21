package p_10813;


import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] baskets = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            baskets[i] = i;
        }
        for (int k = 0; k < M; k++) {
            int i = sc.nextInt();
            int j = sc.nextInt();
            int tmp = baskets[i];
            baskets[i] = baskets[j];
            baskets[j] = tmp;
        }
        for (int i = 1; i < baskets.length; i++) {
            System.out.print(baskets[i] + " ");
        }
    }
}
