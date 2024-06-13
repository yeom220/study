package p_1427;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        String str = new Scanner(System.in).next();
        String[] strs = str.split("");
        Arrays.sort(strs, Collections.reverseOrder());
        for (String s : strs) {
            System.out.print(s);
        }
    }
}
