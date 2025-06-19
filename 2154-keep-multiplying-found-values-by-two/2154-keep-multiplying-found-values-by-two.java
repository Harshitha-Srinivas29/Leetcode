class Solution {
    public int findFinalValue(int[] nums, int original) {
        HashSet<Integer> h = new HashSet<>();

         for(int n : nums){
            h.add(n);
         }

        while(h.contains(original)){
            original *= 2;
        }

        return original;
    }
}