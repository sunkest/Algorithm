import java.util.ArrayList;

public class N_Presentation {
    ArrayList<ArrayList<Integer>> pool;
    public static void main(String[] args) {
        N_Presentation n = new N_Presentation();
        System.out.println(n.solution(5, 12));
    }
    public int solution(int N, int number){
        pool = new ArrayList<>();
        for(int i=0; i<9; i++){
            pool.add(new ArrayList<Integer>());
        }
        //pool.get(0) is EMPTY
        int answer = -1;
        pool.get(1).add(N);
        for(int i=2; i<=8; i++){
            ArrayList<Integer> ith_pool = pool.get(i);
            for(int a=1; a<i; a++){
                int b = i-a;
                for(int e1 : pool.get(a)){
                    for(int e2: pool.get(b)){
                        StringBuilder str = new StringBuilder();
                        for(int n=0; n<i; n++){
                            str.append(String.valueOf(N));
                        }
                        ith_pool.add(Integer.parseInt(str.toString()));
                        ith_pool.add(e1+e2);
                        ith_pool.add(e1-e2);
                        ith_pool.add(e1*e2);
                        if(e2 != 0) ith_pool.add(e1/e2);
                    }
                }
            }
        }

        for(int i=1; i<9; i++){
            if(pool.get(i).contains(number)){
                answer = i;
                break;
            }
        }
        return answer;
    }
}
