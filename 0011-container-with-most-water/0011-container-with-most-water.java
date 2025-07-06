class Solution {
    public int maxArea(int[] height) {
       int left = 0, right = height.length-1;
       int maxWater = Integer.MIN_VALUE;

       while(left < right){
        if(height[left] < height[right])
        {   
            maxWater = Math.max(maxWater, (right-left) * height[left]);
            left++;
        } else{
            maxWater = Math.max(maxWater, (right-left) * height[right]);
            right--;
        }
       } 
       return maxWater;
    }
}