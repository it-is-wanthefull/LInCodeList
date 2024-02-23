import java.io.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader((new InputStreamReader(System.in)));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(bf.readLine());
        int n_yak = Integer.parseInt(st.nextToken());

        ArrayList<Integer> yak = new ArrayList<>();

        st = new StringTokenizer(bf.readLine());
        for(int i=0; i<n_yak; i++)
            yak.add(Integer.parseInt(st.nextToken()));

        Collections.sort(yak);
        bw.write(yak.get(0) * yak.get(n_yak-1) +"\n");
        bw.close();
    }
}