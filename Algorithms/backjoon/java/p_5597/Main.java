package p_5597;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        boolean[] attendance = new boolean[31];

        Scanner sc = new Scanner(System.in);
        for (int i = 0; i < 28; i++) {
            int studentId = sc.nextInt();
            attendance[studentId] = true;
        }
        for (int i = 1; i < attendance.length; i++) {
            if (!attendance[i]) {
                System.out.println(i);
            }
        }
    }
}
