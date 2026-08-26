class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        a=bin(n)
        nums=a[2:]
        for num in nums:
          if num =='0':
            continue
          else:
            count+=1
        return count