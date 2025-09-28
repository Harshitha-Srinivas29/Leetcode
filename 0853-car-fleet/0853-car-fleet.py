class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed))
        stack = []

        for pos, sp in pair[::-1]:
            distance = target - pos
            if not stack:
                stack.append(distance/sp)
            elif distance/sp > stack[-1]:
                stack.append(distance/sp)
        return len(stack)