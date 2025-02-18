class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
       Arrays.sort(nums);
       ArrayList<Integer> list = new ArrayList<>();
       List<List<Integer>> result = new ArrayList<>();
       boolean[] visited = new boolean[nums.length];

       recursiveCall(nums, visited, list, result);
       return result;

    }

    public void recursiveCall(int[] nums, boolean[] visited, ArrayList<Integer> list, List<List<Integer>> result){
         if(list.size() == nums.length){
            result.add(new ArrayList<>(list));
            return;
        }

        for(int i=0; i<nums.length; i++){

            if(visited[i] == true){
                continue;
            }

            if(i>0 && nums[i] == nums[i-1] && visited[i-1] == false)
                continue;

            visited[i] = true;
            list.add(nums[i]);
            recursiveCall(nums, visited, list, result);
            list.remove(list.size()-1);
            visited[i] = false;
        }
    }
}