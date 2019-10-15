class Solution {
    public int distributeCandies(int[] candies) {
        HashSet<Integer> unique = new HashSet<>();
        for(int i = 0; i < candies.length; i ++){
            unique.add(candies[i]);
        }

        return Math.min(unique.size(), candies.length/2);
    }
}
