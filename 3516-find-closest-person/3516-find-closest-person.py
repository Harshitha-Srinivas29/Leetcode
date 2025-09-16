class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(z-x) > abs(y-z):
            return 2
        elif abs(z-x) == abs(y-z):
            return 0
        else:
            return 1