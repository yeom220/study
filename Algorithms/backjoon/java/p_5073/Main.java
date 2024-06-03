package p_5073;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true){
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            if (a == 0 && b == 0 && c == 0) break;
            int[] lines = {a, b, c};
            Arrays.sort(lines);

            if(a == b && a == c){
                System.out.println("Equilateral");
            }else if(lines[2] >= lines[0] + lines[1]){
                System.out.println("Invalid");
            }else if(a != b && a != c && b != c){
                System.out.println("Scalene");
            }else{
                System.out.println("Isosceles");
            }
        }
    }
}
