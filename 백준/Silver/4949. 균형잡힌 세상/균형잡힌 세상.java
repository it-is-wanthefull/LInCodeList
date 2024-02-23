import java.io.*;
import java.util.Stack;

public class Main {
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        while(true){
            Stack<Character> my_stack = new Stack<Character>();
            int smlCount = 0;
            int bigCount = 0;
            String input = br.readLine();

            if(input.equals(".")) break;

            for(int i=0; i<input.length(); i++){
                char c = input.charAt(i);
                if(c == '.')                                                                        {                    break; }
                else if(c == '(')                                                                   { my_stack.push(c);         }
                else if(c == '[')                                                                   { my_stack.push(c);         }
                else if(c == ')' && ( my_stack.empty()            || my_stack.peek().equals('[') )) { my_stack.push(c);  break; }
                else if(c == ')' && ( my_stack.peek().equals('('))                                ) { my_stack.pop();           }
                else if(c == ')' && ( my_stack.peek().equals(')') || my_stack.peek().equals(']') )) { my_stack.push(c);         }
                else if(c == ']' && ( my_stack.empty()            || my_stack.peek().equals('(') )) { my_stack.push(c);  break; }
                else if(c == ']' && ( my_stack.peek().equals('['))                                ) { my_stack.pop();           }
                else if(c == ']' && ( my_stack.peek().equals(')') || my_stack.peek().equals(']') )) { my_stack.push(c);         }
            }
            if(my_stack.empty()) bw.write("yes\n");
            else                 bw.write("no\n");
        }
        bw.close();
    }
}