class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        sol = []
        d = {}
        for i in range(len(mat)):  # Outer loop iterates through each row (inner list)
            for j in range(len(mat[i])):  # Inner loop iterates through each element in the current row
                d.setdefault(i+j,[]).append(mat[i][j])

        for k in sorted(d.keys()):
            vals = d[k]
            if k % 2 == 0:
                vals = reversed(vals)
            for x in vals:
                sol.append(x)
        return sol
        