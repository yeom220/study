package p_9063;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int xMin = 100001;
        int yMin = 100001;
        int xMax = -100001;
        int yMax = -100001;

        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            xMin = Math.min(xMin, x);
            yMin = Math.min(yMin, y);
            xMax = Math.max(xMax, x);
            yMax = Math.max(yMax, y);
        }
        int xLine = xMax - xMin;
        int yLine = yMax - yMin;
        System.out.println(xLine * yLine);
    }
}
