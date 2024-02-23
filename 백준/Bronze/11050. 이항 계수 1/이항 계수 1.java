import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int k_copy = k;
        int answer = 1;

        while(k_copy-- > 0)
            answer *= n--;
        while(k > 0)
            answer /= k--;

        bw.write(answer+"\n");
        bw.close();
    }
}