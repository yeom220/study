package chap_06;
/**
 * 문제
 * 초기에
 * $n+1$개의 집합
 * $\{0\}, \{1\}, \{2\}, \dots , \{n\}$이 있다. 여기에 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
 * <p>
 * 집합을 표현하는 프로그램을 작성하시오.
 * <p>
 * 입력
 * 첫째 줄에
 * $n$,
 * $m$이 주어진다.
 * $m$은 입력으로 주어지는 연산의 개수이다. 다음
 * $m$개의 줄에는 각각의 연산이 주어진다. 합집합은
 * $0$
 * $a$
 * $b$의 형태로 입력이 주어진다. 이는
 * $a$가 포함되어 있는 집합과,
 * $b$가 포함되어 있는 집합을 합친다는 의미이다. 두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산은
 * $1$
 * $a$
 * $b$의 형태로 입력이 주어진다. 이는
 * $a$와
 * $b$가 같은 집합에 포함되어 있는지를 확인하는 연산이다.
 * <p>
 * 출력
 * 1로 시작하는 입력에 대해서
 * $a$와
 * $b$가 같은 집합에 포함되어 있으면 "YES" 또는 "yes"를, 그렇지 않다면 "NO" 또는 "no"를 한 줄에 하나씩 출력한다.
 * <p>
 * 제한
 * <p>
 * $1 ≤ n ≤ 1\,000\,000$
 * <p>
 * $1 ≤ m ≤ 100\,000$
 * <p>
 * $0 ≤ a, b ≤ n$
 * <p>
 * $a$,
 * $b$는 정수
 * <p>
 * $a$와
 * $b$는 같을 수도 있다.
 */

import java.util.Scanner;

public class P1717_집합표현하기 {
    public static int[] parent;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        parent = new int[N + 1];
        for (int i = 0; i < parent.length; i++) {   // 대표 노드를 자기 자신으로 초기화
            parent[i] = i;
        }
        for (int i = 0; i < M; i++) {
            int question = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (question == 0) {    // 집합 합치기
                union(a, b);
            } else {    // 같은 집합의 원소인지 확인
                if (checkSum(a, b)) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
    }

    private static void union(int a, int b) {   // union 연산: 대표 노드끼리 연결
        a = find(a);
        b = find(b);
        if (a != b) {
            parent[b] = a;
        }
    }

    private static int find(int a) {    // find 연산: 대표 노드 찾기
        if (a == parent[a]) return a;
        else return parent[a] = find(parent[a]);    // 재귀 함수 형태로 구현 -> 경로 압축 부분
    }

    private static boolean checkSum(int a, int b) { // 두 원소가 같은 집합인지 확인
        a = find(a);
        b = find(b);
        if (a == b) {
            return true;
        }
        return false;
    }
}
