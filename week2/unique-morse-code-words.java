//maria diaz
//unique-morse-code-words
class Solution {
    public int uniqueMorseRepresentations(String[] words) {
         String[] alph ={".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."} ;

        //imc short for international morse code
           HashSet<String> transformations = new HashSet<>();


    //Decode each word and add the decoding in to set
        for(int i = 0; i < words.length; i++){
             String decoded = "";
            //decode each word
            String word = words[i].toLowerCase();
        for(int j = 0; j < word.length(); j ++){
            decoded += alph[word.charAt(j) - 'a'];
        }
            transformations.add(decoded);

        }
        return transformations.size();

    }

}
