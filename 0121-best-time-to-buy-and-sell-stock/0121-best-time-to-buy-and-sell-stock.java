class Solution {
    public int maxProfit(int[] prices) {
        int maxDiff = 0, min = prices[0];
        for(int i=1; i<prices.length; i++){
            if(prices[i] < min){
                min = prices[i];
            } else {
                maxDiff = Math.max(prices[i]-min, maxDiff);
            }
        }
        return maxDiff;
    }
}