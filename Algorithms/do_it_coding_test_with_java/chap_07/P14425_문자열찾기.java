package chap_07;

import java.util.Scanner;

public class P14425_문자열찾기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        TNode root = new TNode();
        while (n > 0) {
            String text = sc.next();    // 트라이 자료구조 구축하기
            TNode now = root;
            for (int i = 0; i < text.length(); i++) {
                char c = text.charAt(i);
                // 26개 알파벳의 위치를 배열 index로 나타내기 위해 -'a'수행하기
                if (now.next[c - 'a'] == null) {
                    now.next[c - 'a'] = new TNode();
                }
                now = now.next[c - 'a'];
                if (i == text.length() - 1)
                    now.isEnd = true;
            }
            n--;
        }
        int count = 0;
        while (m > 0) { // 트라이 자료구조 검사하기
            String text = sc.next();
            TNode now = root;
            for (int i = 0; i < text.length(); i++) {
                char c = text.charAt(i);
                if (now.next[c - 'a'] == null) {    // 공백 노드라면 이 문자열을 포함하지 않음
                    break;
                }
                now = now.next[c - 'a'];
                if (i == text.length() - 1 && now.isEnd) {  // 문자열의 끝이고 현재까지 모두 일치하면
                    count++;                                // S 집합에 포함되는 문자열
                }
            }
            m--;
        }
        System.out.println(count);
    }
}

class TNode {
    TNode[] next = new TNode[26];
    boolean isEnd;  // 문자열의 마지막 유무를 표시하기
}
