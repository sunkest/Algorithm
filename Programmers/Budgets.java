public class Budgets {
    public static void main(String[] args) {
        Budgets b = new Budgets();
        int[] budgets = {120,110,140,150};
        System.out.println(b.solution(budgets, 485));
    }

    public int solution(int[] budgets, int M) {
        long sum = 0;
        int max = -1;
        for(int b : budgets){
            sum += b;
            if(b > max) max = b;
        }


        if(sum <= M){
            return max;
        }

        int a = 1;
        int b = max;
        int mid = (a+b) / 2;
        while(a <= b){
            System.out.println(a+","+b);
            long midsum = 0;
            for(int x :budgets){
                midsum += Math.min(x, mid);
            }
            if(midsum > M) b = mid-1;
            else a = mid+1;
            mid = (a+b) / 2;
        }


        return mid;
    }
}
