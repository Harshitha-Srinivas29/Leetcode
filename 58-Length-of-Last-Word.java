class Solution {
    public int lengthOfLastWord(String s) {
        
        int count = 0;
        s = s.trim();
        int n = s.length()-1;
        while(n>=0){
            if(s.charAt(n)!= ' '){
                count++;
                n--;
            }
            else if(count>0)
                break;

        }
        return count;
    }
}