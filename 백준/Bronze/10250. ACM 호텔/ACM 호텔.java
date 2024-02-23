import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int customer = scanner.nextInt();
        for (int i = 0; i < customer; i++) {
            int h = scanner.nextInt();
            int w = scanner.nextInt();
            int n = scanner.nextInt();
            int answer = 0;

            if (n % h == 0)     answer =      h  * 100 + (n / h);
            else                answer = (n % h) * 100 + (n / h + 1);
            
            System.out.println(answer);
        }
    }
}