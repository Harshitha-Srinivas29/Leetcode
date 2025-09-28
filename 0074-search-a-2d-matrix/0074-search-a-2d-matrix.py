class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [item for row in matrix for item in row]
        left, right = 0, len(flat_list)-1
        while left <= right:
            mid = (right+left)//2
            if flat_list[mid] == target:
                return True
            elif flat_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
        