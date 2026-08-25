class Solution:
    def addBinary(self, a: str, b: str) -> str:
        val_1=int(a[2:],2) if a.startswith('0b') else int(a, 2)
        val_2=int(b[2:],2) if b.startswith('0b') else int(b, 2)
        result=bin(val_1+val_2)
        return result[2:]