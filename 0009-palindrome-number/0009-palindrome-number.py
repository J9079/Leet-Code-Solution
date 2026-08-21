class Solution:
    def isPalindrome(self, x: int) -> bool:
# Brutal Approach 
    #  if x<0:
    #     return False
    #  rev=0
    #  n=x
    #  while x>0:
    #     digit=x%10 
    #     rev = rev *10 + digit
    #     x = x//10
    #  return rev == n       

# optimal Approach

        if x < 0 or (x % 10 == 0 and x != 0):
            return False        
        rev = 0
        while x > rev:        
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10          
    