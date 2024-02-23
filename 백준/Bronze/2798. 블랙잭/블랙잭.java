import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int big = -1;
        int[] card = new int[n];

        st = new StringTokenizer(bf.readLine());
        for(int i=0; i<n; i++)
            card[i] = Integer.parseInt(st.nextToken());
        Arrays.sort(card);

        for(int i=0; i<n; i++) {
            for(int j=i+1; j<n; j++) {
                for(int k=j+1; k<n; k++) {
                    if     (m == card[i]+card[j]+card[k])       { big = m;   break;              }
                    else if(m  > card[i]+card[j]+card[k]
                              && card[i]+card[j]+card[k] > big) { big = card[i]+card[j]+card[k]; }
                }
            }
        }
        bw.write(big+"\n");
        bw.close();
    }
}