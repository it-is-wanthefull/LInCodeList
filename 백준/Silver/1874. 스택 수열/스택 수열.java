import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder answer = new StringBuilder(); //메모리초과 이슈로 String.concat() 대신 StringBuilder.append()

        Stack<Integer> my_stack = new Stack<Integer>();
        int push_max;
        int rest_target = push_max = sc.nextInt();
        int target = sc.nextInt();  rest_target--;  //새 타겟을 받을때마다 감소

        for(int i=1; i<=push_max; i++) {
            my_stack.push(i);
            answer.append("+\n");

            while( !my_stack.empty() && my_stack.peek()==target ) {
                my_stack.pop();
                answer.append("-\n");
                
                if(rest_target-- > 0)
                    target = sc.nextInt();
            }
        }

        if(my_stack.empty()) System.out.println(answer);
        else                 System.out.println("NO");
    }
}