import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int input = Integer.parseInt(br.readLine());

        if (input == 4 || input == 7) { System.out.println(-1);       } // 5kg/3kg로 나누어 담을 수 없는 절대예외 에러처리(-1)
        else { switch (input % 5)     {                                 // 14kg 등은 5로나눈후 3으로또나누는 단순방법 불가하기에 패턴을 찾으면
                case 0:                 System.out.println(input/5    ); break;
                case 1: case 3:         System.out.println(input/5 + 1); break;
                case 2: case 4:         System.out.println(input/5 + 2); break;
            }
        }
        br.close();
    }
}