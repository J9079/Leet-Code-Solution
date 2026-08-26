class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for index,num in enumerate(nums):
          valid=target-num
          if valid in result:
            return [result[valid],index]
          result[num]=index
        return 