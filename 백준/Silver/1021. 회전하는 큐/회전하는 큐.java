import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int answer = 0;

        int q_max = sc.nextInt();
        int q_size = q_max;
        int q_front = 0;
        boolean[] q = new boolean[q_max]; // pop되면 false
        Arrays.fill(q, true);         // q 초기화

        int total_command = sc.nextInt();
        for(int i=1; i<=total_command; i++) {
            int target = sc.nextInt() - 1;
            int distance = target - q_front;
            int n_move = 0;

            if( distance==0 ) { }  // 이동이 없으므로 노카운트
            else if( (distance>0 && distance<=(double)(q_max/2))
                  || (distance<0 && distance>=(double)(q_max/2)) ) {
                for(int j=q_front+1; distance--!=0; j++) {
                    j = (j+q_max) % q_max; // 오버플로우 방지
                    if(q[j] == true) {
                        n_move++;
                    }
                }
            }
            else if( (distance>0 && distance>(double)(q_max/2))
                  || (distance<0 && distance<(double)(q_max/2)) ) {
                for(int j=q_front-1; (q_max-distance++)%q_max!=0; j--) {
                    j = (j+q_max) % q_max; // 오버플로우 방지
                    if(q[j] == true) {
                        n_move++;
                    }
                }
            }
            if((double)(q_size/2) >= n_move) answer += n_move;
            else                               answer += q_size - n_move;
            q[target] = false;
            if(--q_size != 0)
                while(q[ (++target + q_max) % q_max ] != true) { } // target장소만 물색하는 반복문
            q_front = (target + q_max) % q_max;
        }
        System.out.println(answer);
    }
}