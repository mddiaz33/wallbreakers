
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> set1 = new HashSet<>();
        HashSet<Integer> intersec = new HashSet<>();
        //convert nums1 into a set
        for(int num1 : nums1){
            set1.add(num1);
        }
        //if a number in nums2 is in set 1 then add it to Intersection
       for(int num2 : nums2){
            if(set1.contains(num2))
                intersec.add(num2);
       }

        int[] ans = new int[intersec.size()];
        int i = 0;
        //turn intersection into an array for returning
        for(int num: intersec){
                ans[i++] = num;
            }
        return ans;
    }
}
