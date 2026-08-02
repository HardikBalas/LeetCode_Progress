class Solution(object):
    def isPalindrome(self, x):
        if x < 0 :
            return False
        num = x
        rev_num = 0
        while x > 0:
            last_num = x%10
            rev_num = rev_num*10 + last_num
            x = x//10
        if num == rev_num:
            return True
        else:
            return False