class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        f=0
        l=len(arr)-1
        while f<l:
          mid=(f+l)//2
          if arr[mid]<=arr[mid+1]:
            f=mid+1
          else:  
            l=mid
        return l        