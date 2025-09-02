class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hmap = new HashMap<>();

        for(int i=0; i<nums.length; i++){
            int remainder = target - nums[i];
            if(hmap.containsKey(remainder))
                return new int[] {i, hmap.get(remainder)};

            hmap.put(nums[i], i);
        }

        return new int[] {-1, -1};
    }
}