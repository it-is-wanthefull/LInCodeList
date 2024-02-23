import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 화폐 단위 입력 받기
        int[] money = new int[n];
        int lastIndex =0;
        int answer = 0;
        for (int i = 0; i < n; i++) {
            int moneyValue = Integer.parseInt(br.readLine());
            if (moneyValue <= k) {
                money[i] = moneyValue;
                lastIndex = i;
            }
        }

        // 큰 화폐 단위부터 나누기
        for (int i = lastIndex; i >= 0; i--){
            if (k / money[i] > 0) {
                answer += k / money[i];
                k = k % money[i];
            }
            if (k ==0) {
                break;
            }
        }
        System.out.println(answer);
    }
}