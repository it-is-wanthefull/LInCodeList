import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int upupA = sc.nextInt();
        int downB = sc.nextInt();
        int highV = sc.nextInt();
        int answer = (int)Math.ceil( ( (double)(highV - upupA) / (double)(upupA - downB) ) ) + 1;

        System.out.println(answer);
    }
}