//문제1110: 더하기 사이클
//0보다 크거나 같고, 99보다 작거나 같은 정수가 주어질 때 다음과 같은 연산을 할 수 있다. 먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다. 다음 예를 보자.
//26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.
//위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.
//N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
//
//입력: 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수이다.
//출력: 첫째 줄에 N의 사이클 길이를 출력한다.
//
//입력 > 출력
//26 > 4
//55 > 3
//1 > 60
//0 > 1
//71 > 12
//
//
//
//
//
//
//
//
//풀이
//
// 2자리(ex 68) (n%10)*10 + ((n/10+n%10)%10)
// 1자리(ex 3) (n)*10 + n
//
// next = b * 10 + (a+b) % 10
//
//
// input 기억, 바뀐횟수 i 기억, change_value 기억
// input과 change_value 비교 같으면 i 출력
//
// 2 22 24 46 60 06 66
//
//
//

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int input = sc.nextInt();
        int a = input / 10; //십의자리
        int b = input % 10; //일의자리
        int i = 0; //반복횟수
        int change_value = 0; //바뀐값 임시저장소
        //System.out.println(i+ " "+input + " "+ a+" "+ b);
        do {
            change_value = b * 10 + (a + b) % 10;

            // a,b 새로운 값 부여
            a = change_value / 10; //십의자리
            b = change_value % 10; //일의자리

            i++;
            //System.out.println(i+" "+change_value + " "+ a+" "+ b);
        } while(input != change_value);

        System.out.println(i);
    }
}