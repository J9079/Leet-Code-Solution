class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # dec={}
        # for index, num in enumerate(numbers):
        #   valid=target-num
        #   if valid in dec:
        #     return [dec[valid],index+1]
        #   dec[num]=index+1
        # return dec        
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else: 
                right -= 1
        return []        