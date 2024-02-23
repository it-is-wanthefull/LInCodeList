import java.io.InputStreamReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int total_command = Integer.parseInt(bf.readLine());
        int answer = 0;
        Stack<Integer> my_stack = new Stack<>();

        for(int i=0; i<total_command; i++){
            int input = Integer.parseInt(bf.readLine());
            if(input == 0) my_stack.pop();
            else           my_stack.push(input);
        }

        while(!my_stack.empty())
            answer += my_stack.pop();

        System.out.println(answer);
    }
}