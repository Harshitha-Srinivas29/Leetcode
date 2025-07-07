class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        int max = 0, maxCount = 0;

        for(char task : tasks){
            freq[task - 'A']++;
            max = Math.max(freq[task-'A'], max);
        }

        for(int i: freq){
            if(i == max) maxCount++;
        }
        return Math.max(tasks.length, (max-1) * (n+1) + maxCount);
    }
}