package alps.skyoo;

import java.util.Scanner;

public class Q2156 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		
		int n = scan.nextInt();
		int w[] = new int[n]; //���� ��
		int d[] = new int[n]; //n��°������ �ִ�
		for(int i=0; i<n; i++) {
			w[i] = scan.nextInt();
		}
		
		//d[n]�� d[n-3]+w[n-1]+w[n], d[n-2]+w[n], d[n-1] �� �ִ�
		//d[0] = w[0] //d[1] = w[0]+w[1] //d[2] = �����߿� �������Ż���
		
		d[0] = w[0];
		d[1] = w[0]+w[1];
		d[2] = w[0]+ w[1]+ w[2] - Math.min(Math.min(w[0], w[1]), w[2]);
		
		for(int i=3; i<n; i++) {
			int m = Math.max(d[i-1], d[i-2]+w[i]);
			d[i] = Math.max(m, d[i-3]+w[i-1]+w[i]);
		}
		System.out.println(d[n]);
		
		
	}

}
