import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Integer> input = new ArrayList<>();

        do {
            input.add(sc.nextInt());
        } while (!input.contains(0)); // EOF조건(=0)확인

        for (int input_index=0; input_index<input.size()-1; ++input_index) {
            int answer = 0;

            for (int divided=(Integer)input.get(input_index)+1; divided<=(Integer)input.get(input_index)*2; ++divided) {
                boolean isPrime = true;

                for (int divisor=2; divisor<=Math.sqrt(divided); ++divisor) {
                    if (divided % divisor == 0) {
                        isPrime = false;
                        break;
                    }
                }

                if (isPrime) answer++;
            }

            System.out.println(answer);
        }
    }
}