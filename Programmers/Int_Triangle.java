import java.util.Arrays;

public class Int_Triangle {
    int[][] table;

    public static void main(String[] args) {
        Int_Triangle t = new Int_Triangle();
        int[][] input = {{7}, {3,8}, {8,1,0}, {2,7,4,4}, {4,5,2,6,5}};
        System.out.println(t.solution(input));
    }

    public int solution(int[][] triangle){
        table = new int[triangle.length][];
        for(int i=0; i<triangle.length; i++){
            table[i] = new int[triangle[i].length];
            Arrays.fill(table[i], -1);
        }
        table[0][0] = triangle[0][0];
        for(int i=0; i<triangle[triangle.length-1].length; i++){
            dp(triangle.length-1, i, triangle);
        }

        Arrays.sort(table[table.length-1]);
        return table[table.length-1][table[table.length-1].length-1];
    }

    public int dp(int a, int b, int[][] triangle){
        if(table[a][b] != -1){
            return table[a][b];
        }
        else{
            if(b==0){
                table[a][b] = dp(a-1, b, triangle) + triangle[a][b];
                return table[a][b];
            }
            else if(b==a){
                table[a][b] = dp(a-1, b-1, triangle) + triangle[a][b];
                return table[a][b];
            }
            else{
                table[a][b] = Math.max(dp(a-1, b-1, triangle), dp(a-1, b, triangle)) + triangle[a][b];
                return table[a][b];
            }
        }
    }

}
