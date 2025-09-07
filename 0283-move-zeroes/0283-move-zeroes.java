class Solution {
    public void moveZeroes(int[] nums) {
        int i =0;
        int j = nums.length-1;

        if(j==0)
            return;

        while(i<j){
            if(nums[i] != 0)
                i++;
            else{
                for(int k=i; k<j; k++){
                    int temp = nums[k];
                    nums[k] = nums[k+1];
                    nums[k+1] = temp;
                }
                j--;
            }
        }
    }
}