class Solution {
    public String[] uncommonFromSentences(String A, String B) {
        //add string together so you only need to iterate thru one
        String str = A+" "+ B;
        //split by white space
        String[] arr = str.split(" ");
        HashMap<String, Boolean> words = new HashMap<>();
        //add each word to has map
        for(int i = 0; i < arr.length;i++){
            //if word not in map set value to true
            if (!words.containsKey(arr[i]))
                words.put(arr[i], true);
            //if already in map set value = false
            else
                words.put(arr[i], false);
        }
        //prepare empty array for return
        String[] empty = {} ;
        //get unique words in set
        String uniqueWords = getUniqueWords(words);
        //return empty array or array of words
         return uniqueWords.equals("") ?  empty: uniqueWords.split(" ");

}
    //search for unique words in dictionary
    public String getUniqueWords(HashMap<String,Boolean> words){
        String str = "";
        for (Map.Entry<String, Boolean> entry : words.entrySet()) {
                  if (entry.getValue())
                    str += entry.getKey()+" ";

         }
        return str;
    }
}
