class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = -1
        max_area = -1
        for a, b in dimensions:
            diagonal = sqrt(a**2 + b**2)
            area = a*b
            print(area)
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = area
            elif diagonal == max_diagonal:
                max_diagonal = diagonal
                max_area = max(area, max_area)
        return max_area

        
