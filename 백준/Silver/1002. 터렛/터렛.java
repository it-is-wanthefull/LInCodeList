import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int testcase = sc.nextInt();
        int[] output = new int[testcase];

        for(int i=1; i<=testcase; i++) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int r1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();
            int r2 = sc.nextInt();
            double d = Math.sqrt(Math.pow(x1-x2, 2) + Math.pow(y1-y2, 2));

            if(d == 0) {
                if(r1 == r2) {
                    output[i-1] = -1;
                }
                else {
                    output[i-1] = 0;
                }
            } else if(d == r1 + r2 || d == Math.abs(r1 - r2)) {
                output[i-1] = 1;
            } else if(d > r1 + r2 || d < Math.abs(r1 - r2)) {
                output[i-1] = 0;
            } else if(d < r1 + r2 || d > Math.abs(r1 - r2)) {
                output[i-1] = 2;
            }
            else output[i-1] = -1;
        }

        for(int i=1; i<=testcase; i++) {
            System.out.println(output[i-1]);
        }
    }
}