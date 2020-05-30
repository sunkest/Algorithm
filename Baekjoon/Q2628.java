package alps.skyoo;

import java.io.IOException;
import java.util.Collections;
import java.util.Scanner;
import java.util.Vector;

public class Q2628 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		Scanner scan = new Scanner(System.in);
		int x,y;
		x = scan.nextInt();
		y = scan.nextInt();
		int n;
		n = scan.nextInt();
		Vector<Integer> a = new Vector<Integer>();
		Vector<Integer> b = new Vector<Integer>();
		a.add(0);
		a.add(y);
		b.add(0);
		b.add(x);
		
		for(int i=0; i<n; i++) {
			if(scan.nextInt() == 0) {	//°¡·Î
				a.add(scan.nextInt());
			}else b.add(scan.nextInt());
		}
		Collections.sort(a);
		Collections.sort(b);
//		System.out.println(a.toString());
//		System.out.println(b.toString());
		
		int maxA = 0;
		int maxB = 0;
		for(int i=1; i<a.size(); i++) {
			if(maxA<(a.get(i)-a.get(i-1))) maxA = a.get(i)-a.get(i-1);
		}
		for(int i=1; i<b.size(); i++) {
			if(maxB<(b.get(i)-b.get(i-1))) maxB = b.get(i)-b.get(i-1);
		}
		if(maxA == 0) maxA = x;
		if(maxB == 0) maxB = y;
		System.out.println(maxA*maxB);
	}
}
