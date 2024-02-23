import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st/* = new StringTokenizer(bf.readLine())*/;
        StringTokenizer st_in_st;
        int answer = 0;
        int answer_of_part = 0;
        boolean isFirst = true;

        st = new StringTokenizer(bf.readLine(), "-");
        while(st.hasMoreTokens()) {
            st_in_st = new StringTokenizer(st.nextToken(), "+");

            answer_of_part = 0;
            while(st_in_st.hasMoreTokens())
                answer_of_part += Integer.parseInt(st_in_st.nextToken());
            
            if(isFirst) { answer += answer_of_part; isFirst = false; }
            else        { answer -= answer_of_part;                  }
        }
        bw.write(answer+"\n");
        bw.close();
    }
}