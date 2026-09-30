class Solution:
    def search(self, nums: list[int], target: int) -> int:
        f=0
        l=len(nums)-1
        while f<=l:
          mid=(f+l)//2
          if nums[mid]==target:
            return mid
          if nums[f]<=nums[mid]:
            if nums[f]<=target and target<=nums[mid]:
              l=mid
            else:
              f=mid+1
          else:
            if nums[mid+1]<=target and target<=nums[l]:
              f=mid+1
            else:
              l=mid
        return -1              