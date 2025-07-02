class Solution {
    public String[] findWords(String[] words) {
        String[] rows = {
            "qwertyuiopQWERTYUIOP",
            "asdfghjklASDFGHJKL",
            "zxcvbnmZXCVBNM"
        };

        List<String> ans = new ArrayList<>();
        for(String word : words){
            char[] c = word.toCharArray();
            if(possibleWord(c, rows[0]) || possibleWord(c, rows[1]) || possibleWord(c, rows[2])){
                ans.add(word);
            }
        }
        return ans.toArray(new String[0]);        
    }

    public boolean possibleWord(char[] c, String row){
        for(char c1 : c){
            if(row.indexOf(c1) == -1)
                return false;
        }

        return true;
    }
}