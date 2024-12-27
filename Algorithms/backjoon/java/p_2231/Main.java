package p_2231;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        int n = String.valueOf(input).length();
        int s = input - (n*9);
        if (s < 0) {
            s = 0;
        }
        int e = input + (n*9);

        int result = 0;
        for (int i = s; i <= e; i++){
            int sum = sum(i);
            if (sum == input){
                result = i;
                break;
            }
        }
        System.out.println(result);
    }

    public static int sum (int n){
        String[] strs = String.valueOf(n).split("");
        int sum = 0;
        for (String str : strs) {
            sum += Integer.parseInt(str);
        }
        return sum + n;
    }
}
