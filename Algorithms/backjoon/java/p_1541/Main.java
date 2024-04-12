package p_1541;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] strs = sc.nextLine().split("-");
        int plus = 0;
        int minus = 0;
        for(int i=0; i<strs.length; i++){
            if(i == 0){
                for(String s : strs[i].split("[+]")){
                    plus += Integer.parseInt(s);
                }
            }
            else {
                for(String s : strs[i].split("[+]")){
                    minus += Integer.parseInt(s);
                }
            }
        }
        System.out.println(plus - minus);
    }
}
