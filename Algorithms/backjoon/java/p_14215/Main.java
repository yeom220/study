package p_14215;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int[] lines = {a, b, c};
        Arrays.sort(lines);
        int max = lines[2];
        int mod = lines[0] + lines[1];
        if (max >= mod) {
            int diff = max - mod + 1;
            max -= diff;
        }
        System.out.println(max + mod);
    }
}
