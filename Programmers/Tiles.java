import java.awt.color.ICC_Profile;
import java.util.ArrayList;
import java.util.HashMap;

public class Tiles {
    long[] fib;

    public static void main(String[] args) {
        Tiles t = new Tiles();
        System.out.println(t.solution(3));
    }

    public long solution(int N) {
        long answer = 0;
        fib = new long[81];
        fib[1] = 1;
        fib[2] = 1;
        if(N == 1) answer = 4;
        else{
            long a = fibonacci(N);
            long b = fib[N-1];
            answer = 2*(a+a+b);
        }



        return answer;
    }

    public long fibonacci(int n){
        if(fib[n] != 0){
            return fib[n];
        }
        if(n == 1) return 1;
        else if(n == 2) return 1;
        else{
            fib[n] = fibonacci(n-1) + fibonacci(n-2);
            return fib[n];
        }
    }
}
