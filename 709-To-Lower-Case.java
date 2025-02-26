class Solution {
    public String toLowerCase(String s) {
        
        int i = 0;
        StringBuilder sb = new StringBuilder();

        while(i < s.length()){
            char c = s.charAt(i);
            if(c >= 'A' && c <= 'Z'){
                c = (char)(c+32);
            }
            sb.append(c);
            i++;
        }

        return sb.toString();
    }
}