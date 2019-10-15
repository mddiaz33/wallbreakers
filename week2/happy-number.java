//maria diaz
class Solution {
    public boolean isHappy(int n) {
        if(n == 0) return false;
        HashSet<Integer> seen = new HashSet<>();

        while(n != 1){
             n = calculate(n);
            if(!seen.add(n))return false;
         }
        return true;

    }
    //method calculates the square of each digits
    public int calculate(int n ){
        String str = n+"";
        int sum = 0;
        for (int i = 0; i < str.length(); i++){
            sum += Math.pow(str.charAt(i)-'0', 2);
        }
        return sum;
    }

}
