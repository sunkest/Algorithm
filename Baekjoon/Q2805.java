package alps.skyoo;

import java.util.Scanner;

public class Q2805 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int n, m;
		n = scan.nextInt();
		m = scan.nextInt();
		long t[] = new long[n];
		long max = 0;
		for(int i=0; i<n; i++) {
			t[i] = scan.nextInt();
			if(max < t[i]) max = t[i];
		}

		long l = 0;
		long r = max;
		long ans = 0;
		//Binary Search
		while(l <= r) {
			long mid = (l+r)/2;
			long sum = 0;
			long sum2 = 0;
			for(long x : t) {
				if(x-mid > 0) sum += (x-mid);
				if(x-(mid+1) > 0) sum2 += (x-(mid+1));
			}
			if(sum >= m) {
				if(ans < mid) ans = mid;
				l = mid+1;
			}else if(sum < m) {
				r = mid-1;
			}
		}
		
		System.out.println(ans);
		
	}
	

}
