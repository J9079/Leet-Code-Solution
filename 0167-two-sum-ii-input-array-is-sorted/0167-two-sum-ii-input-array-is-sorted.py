class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        dec={}
        for index, num in enumerate(numbers):
          valid=target-num
          if valid in dec:
            return [dec[valid],index+1]
          dec[num]=index+1
        return dec        