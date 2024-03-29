package p_10171;

/**
 * 문제
 * 아래 예제와 같이 고양이를 출력하시오.
 *
 * 입력
 * 없음.
 *
 * 출력
 * 고양이를 출력한다.
 */
public class Main {
    public static void main(String[] args) {
        String[][] cat = {
                {"\\"," "," "," "," ","/","\\"," "},
                {" ",")"," "," ","("," ","'",")"},
                {"("," "," ","/"," "," ",")"," "},
                {" ","\\","(","_","_",")","|"," "},
        };
        for (int i = 0; i < cat.length; i++) {
            String[] strings = cat[i];
            for (int j = 0; j < strings.length; j++) {
                System.out.print(strings[j]);
            }
            System.out.println();
        }
    }
}
