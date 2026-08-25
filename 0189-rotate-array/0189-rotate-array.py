class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        l=k-1
        i=0
        j=len(nums)-1
        while i<j:
          temp=nums[i]
          nums[i]=nums[j]
          nums[j]=temp
          i+=1
          j-=1
        j=len(nums)-1 
        while k<j:
          temp=nums[k]
          nums[k]=nums[j]
          nums[j]=temp
          k+=1
          j-=1
        i=0  
        while i<l:
          temp=nums[i]
          nums[i]=nums[l]
          nums[l]=temp
          i+=1
          l-=1  
        return nums 