class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> fmap = new HashMap<>();

        for(char c: s.toCharArray()){
            fmap.put(c, fmap.getOrDefault(c,0)+1);
        }
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(fmap.get(c) == 1){
                return i;
            }
        }
        return -1;
    }
}