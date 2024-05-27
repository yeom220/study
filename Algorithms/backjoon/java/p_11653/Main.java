package p_11653;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = new Scanner(System.in).nextInt();
        if (n == 1) {
            return;
        }
        int half = n / 2 + 1;
        int[] arr = new int[half];
        List<Integer> answer = new ArrayList<>();
        int index = 2;
        while (n > 1 && index < half) {
            if (arr[index] == 1) {
                index++;
                continue;
            }
            if (n % index == 0) {
                answer.add(index);
                n /= index;
            } else {
                int mul = 1;
                while (index * mul < half) {
                    arr[index * mul++] = 1;
                }
                index++;
            }
        }
        if (answer.isEmpty()) {
            System.out.println(n);
        } else {
            answer.forEach(System.out::println);
        }
    }
}
