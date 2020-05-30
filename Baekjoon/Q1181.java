package alps.skyoo;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Scanner;

public class Q1181  {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int n;
		Scanner scan = new Scanner(System.in);
		n = scan.nextInt();
		HashSet<String> set = new HashSet();
		
		
		for(int i=0; i<n; i++) {
			String str = scan.next();
			set.add(str);
		}
		
		ArrayList<Str> arr = new ArrayList();
		Iterator it = set.iterator();
		while(it.hasNext()) {
			arr.add(new Str((String) it.next()));
		}
		
		
		Collections.sort(arr);
		for(int i=0; i<arr.size(); i++) {
			System.out.println(arr.get(i).str);
		}
			
	}
}

class Str implements Comparable<Str>{
	String str;
	int length;
	Str(String str){
		this.str = str;
		this.length = str.length();
	}
	@Override
	public int compareTo(Str arg0) {
		// TODO Auto-generated method stub
		if(this.length != arg0.length)
			return this.length - arg0.length;
		else
			return this.str.compareTo(arg0.str);
	}
	
}
