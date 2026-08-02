class Solution:
    def romanToInt(self, s):
        Roman = {
            'I':1, 'V':5, 'X':10,
            'L':50, 'C':100, 'D':500, 'M':1000 
        }
        total = 0
        prev = 0
        for i in reversed(s):
            cur = Roman[i]
            if cur < prev:
                total -= cur
            else:
                total += cur
                prev = cur

        return total

        