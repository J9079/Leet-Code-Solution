class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        first=0
        for last in range(len(nums)):
          if  nums[last]!=0:
            nums[first],nums[last]=nums[last],nums[first]
            first+=1
        return nums        