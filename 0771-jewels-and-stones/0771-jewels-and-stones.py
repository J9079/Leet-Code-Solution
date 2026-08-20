class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        lst={}
        count=0
        for i in jewels:
            lst=(i)
            for j in stones:
                if j in lst:
                  count+=1
        return count