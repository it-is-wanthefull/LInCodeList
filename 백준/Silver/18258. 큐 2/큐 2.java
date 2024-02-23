import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int front = 0;
        int back = 0;
        int size = Integer.parseInt(st.nextToken());
        int[] q = new int[size];

        for(int i=0; i<size; i++) {
            st = new StringTokenizer(bf.readLine());

            switch(st.nextToken()) {
                case "push":          q[back++ % size] = Integer.parseInt(st.nextToken());
                    break;
                case "pop":
                    if(front != back) bw.write( q[front++ % size] +"\n" );
                    else              bw.write( -1 +"\n" );
                    break;
                case "front":
                    if(front != back) bw.write( q[front] +"\n" );
                    else              bw.write( -1 +"\n" );
                    break;
                case "back":
                    if(front != back) bw.write( q[(back+size-1) % size] +"\n" );
                    else              bw.write( -1 +"\n" );
                    break;
                case "size":          bw.write( ((back+size) - front) % size +"\n" );
                    break;
                case "empty":
                    if(front == back) bw.write( 1 +"\n" );
                    else              bw.write( 0 +"\n" );
                    break;
            }
        }
        bw.close();
    }
}