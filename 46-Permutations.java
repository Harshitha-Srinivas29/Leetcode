class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> list = new ArrayList<>();
        boolean[] visited = new boolean[nums.length];
        recursiveCall(nums, visited, result, list);

        return result;
    }

    public void recursiveCall(int[] nums, boolean[] visited, List<List<Integer>> result, List<Integer> list){
        if(list.size() == nums.length){
            result.add(new ArrayList<>(list));
            return;
        }

        for(int i=0; i<nums.length; i++){
            if(visited[i] == false){
                visited[i] = true;
                list.add(nums[i]);
                recursiveCall(nums, visited, result, list);
                list.remove(list.size()-1);
                visited[i] = false;
            }
        }
    }
}