/*
------
------
------
1: 1 3 L
------
------
------
1: 1 2 R

2: 1 3    L

1: 2 3 R
------
------
------
1: 1 3 L
2: 1 2    R
1: 3 2 L

3: 1 3       L

1: 2 1 L
2: 2 3    R
1: 1 3 L
------
------
------
1: 1 2 R
2: 1 3    L
1: 2 3 R
3: 1 2      R
1: 3 1 R
2: 3 2    L
1: 1 2 R

4: 1 3          L

1: 2 3 R
2: 2 1   L
1: 3 1 R
3: 2 3      R
1: 1 2 R
2: 1 3   L
1: 2 3 R
------
------
------
*/

import java.io.*;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        BufferedReader bf = new BufferedReader((new InputStreamReader(System.in)));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] index = new int[n];
        Arrays.fill(index, 1);

        bw.write(((int)Math.pow(2,n)-1)+"\n"); //총 이동횟수는 2^n-1로 정해져있음
        hanoi(n, n, index, bw);
        bw.close();
    }
    public static void hanoi(int n, int i, int[] index, BufferedWriter bw) throws IOException {
        if(i != 0) {
            hanoi(n, i-1, index, bw);
            center_hanoi(n, i, index, bw);
            hanoi(n, i-1, index, bw);
        }
    }
    public static void center_hanoi(int n, int i, int[] index, BufferedWriter bw) throws IOException { //홀수는LRLR 짝수는RLRL
        if(i != 0) {
            if      (i % 2 == 1 && n % 2 == 1) move_L(i, index, bw);
            else if (i % 2 == 1 && n % 2 == 0) move_R(i, index, bw);
            else if (i % 2 == 0 && n % 2 == 1) move_R(i, index, bw);
            else if (i % 2 == 0 && n % 2 == 0) move_L(i, index, bw);
        }
    }
    public static void move_L(int i, int[] index, BufferedWriter bw) throws IOException {
        bw.write(index[i-1]+" ");
        if(--index[i-1] == 0) index[i-1] = 3; //overflow처리
        bw.write(index[i-1]+"\n");
    }
    public static void move_R(int i, int[] index, BufferedWriter bw) throws IOException {
        bw.write(index[i-1]+" ");
        if(++index[i-1] == 4) index[i-1] = 1; //overflow처리
        bw.write(index[i-1]+"\n");
    }
}