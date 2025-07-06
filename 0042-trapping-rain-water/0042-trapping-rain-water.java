class Solution {
    public int trap(int[] height) {
        int result = 0;
        int left = 0, right = height.length-1;
        int maxLeft = 0, maxRight = 0;
        while(left <= right){
            if(height[left] <= height[right]){
                if(height[left] >= maxLeft) maxLeft = height[left];
                else result += maxLeft - height[left];
                left++;
            } else {
                if(height[right] >= maxRight) maxRight = height[right];
                else result += maxRight - height[right];
                right--;
            }
        }
        return result;
    }
}