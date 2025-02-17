class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        ArrayList<Integer> input = new ArrayList<>();

        recursiveSubset(nums, 0, result, input);

        return result;
    }

    public void recursiveSubset(int[] nums, int index, List<List<Integer>> result, ArrayList<Integer> input) {
        if(index == nums.length){
            result.add(new ArrayList<>(input));
            return;
        }
        // Exclude the current element and move to the next
        recursiveSubset(nums, index+1, result, input);

        // Include the current element and move to the next
        input.add(nums[index]);
        recursiveSubset(nums, index+1, result, input);

        // Backtrack to remove the last added element
        input.remove(input.size()-1);

    }
}