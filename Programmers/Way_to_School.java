import java.util.Arrays;

public class Way_to_School {
    int[][] map;

    public static void main(String[] args) {
        Way_to_School w = new Way_to_School();
        int[][] puddles = {{2,2},{4,2}};
        System.out.println(w.solution(4,3, puddles));
    }

    public int solution(int m, int n, int[][] puddles) {
        map = new int[m+1][n+1];
        for(int[] pud : puddles) {
            map[pud[0]][pud[1]] = -1;
        }
        for(int i=0; i<m+1; i++){
            map[i][0] = -1;
        }
        for(int i=0; i<n+1; i++){
            map[0][i] = -1;
        }
        int answer = dp(m,n);
        System.out.println(Arrays.deepToString(map));
        return answer;
    }

    public int dp(int m, int n){
        System.out.println(m + "," + n);
        if(map[m][n] == -1) return 0;
        if(map[m][n] != 0) return map[m][n];
        if((m==1 && n==2) || (m==2 && n==1)) {
            map[m][n] = 1;
            return 1;
        }
        //else
        map[m][n] = (dp(m-1,n) + dp(m, n-1)) % 1000000007;
        return map[m][n];
    }
}
