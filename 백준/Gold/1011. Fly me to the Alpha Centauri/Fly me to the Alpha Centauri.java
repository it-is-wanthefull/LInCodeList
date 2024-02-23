import java.util.Scanner;
import java.lang.Math;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        int[] answer = new int[input];
        
        for (int i = 0; i < input; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();


            int k = (int) Math.sqrt(y - x); // 거리 : 6 , k = 2

            if ((y - x) == Math.pow(k, 2)) {
                answer[i] = 2 * k - 1;
            } else if ((y - x) > Math.pow(k, 2) + k) {
                answer[i] = 2 * k + 1;
            } else if ((y - x) <= Math.pow(k, 2) + k) {
                answer[i] = 2 * k;
            }
        }

        for (int i : answer) {
            System.out.println(i);
        }
    }
}