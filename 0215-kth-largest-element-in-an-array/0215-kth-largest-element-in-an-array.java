class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.reverseOrder());
        int result = -1;
        for(int n: nums){
            pq.offer(n);
        }

        for(int i=0; i<k; i++){
            result = pq.poll();
        }

        return result;
    }
}