import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int input = Integer.parseInt(st.nextToken());
        int count = 0;

        for(int i=0; i<=2666799; i++) {
            if(has666(i)) count++;
            if(count == input) { bw.write(i+"\n"); break; }
        }
        bw.close();
    }
    public static boolean has666(int i) {
        while(true) {
            if(i % 1000 == 666) return true;
            i = i / 10;
            if(i < 100) return false;
        }
    }
}