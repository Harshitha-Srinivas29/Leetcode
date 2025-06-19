class Solution {
    public int maxPower(String s) {
        int curr = 1, max = 1;
        for(int i=0; i<s.length()-1; i++){
            if(s.charAt(i) == s.charAt(i+1))
                curr++;
            else
                curr = 1;

            max = Math.max(max, curr);
        }
        return max;
    }
}