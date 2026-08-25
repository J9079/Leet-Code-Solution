class Solution:
    def reverseBits(self, n: int) -> int:
        binary_num=format(n,'032b')  
        rev=binary_num[::-1]
        return int(rev,2)