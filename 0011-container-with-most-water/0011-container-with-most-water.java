class Solution {
    public int maxArea(int[] height) {
       int left = 0, right = height.length-1;
       int maxWater = Integer.MIN_VALUE;

       while(left < right){
        int curr = (right - left) * Math.min(height[left], height[right]);
        maxWater = Math.max(curr, maxWater);
        if(height[left] < height[right])
        {
            left++;
        } else if (height[left] >= height[right]){
            right--;
        }
       } 

       return maxWater;
    }
}