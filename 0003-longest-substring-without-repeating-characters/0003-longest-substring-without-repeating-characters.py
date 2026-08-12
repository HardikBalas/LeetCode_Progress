class Solution:
    def lengthOfLongestSubstring(self,s: str) -> int:
        maxi = 0
        n = len(s)
        for i in range(0,n):
            my_set = set()
            for k in range(i,n):
                if s[k] in my_set:
                    break
                my_set.add(s[k])
                maxi = max(maxi,k-i+1)
        return maxi