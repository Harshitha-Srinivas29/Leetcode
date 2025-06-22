class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int max = 0;
        for (int pile : piles) {
            max = Math.max(pile, max);
        }

        int left = 1; // prevent divide-by-zero
        int right = max;

        while (left < right) {
            int mid = left + (right - left) / 2;

            if (canEat(piles, mid) <= h) {
                right = mid; 
            } else {
                left = mid + 1; 
            }
        }

        return left; 
    }

    private int canEat(int[] piles, int speed) {
        if (speed == 0) return Integer.MAX_VALUE; 

        int hours = 0;
        for (int pile : piles) {
            hours += (pile + speed - 1) / speed;
        }
        return hours;
    }
}
