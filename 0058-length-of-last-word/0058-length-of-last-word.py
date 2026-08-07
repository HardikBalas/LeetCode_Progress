class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lst = s.split()
        if len(lst) == 0:
            return 0
        else:
            return len(lst[-1])