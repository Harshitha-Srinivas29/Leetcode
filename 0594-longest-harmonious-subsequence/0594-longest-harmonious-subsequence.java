class Solution {
    public int findLHS(int[] nums) {
        Arrays.sort(nums);
        int i=0, count =0;
        for(int j=1; j<nums.length;){
            if(nums[j] - nums[i] == 0)
                j++;
            else if(nums[j] - nums[i] == 1){
                count = Math.max(count, j-i+1);
                j++;
            }
            else 
                i++;
        }
        return count;
    }
}