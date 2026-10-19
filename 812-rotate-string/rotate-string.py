class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        print(s)
        print(s+s)
        return len(goal) == len(s) and goal in s+s