//Maria Diaz
class Solution {
    public int numJewelsInStones(String J, String S) {
        int numberOfGems = 0;
        HashSet<Character> gems = new HashSet<Character>();
        for(int i = 0; i < J.length() ; i++){
            gems.add(J.charAt(i));
        }
        for(int i = 0; i < S.length(); i++){
            if(gems.contains(S.charAt(i))){
                numberOfGems++;
            }
        }
        return numberOfGems;
    }
}
