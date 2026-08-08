# Question 1
# Link - https://leetcode.com/problems/remove-element/
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# def removeElement(nums,val):
#   j=0
#   for i in range(len(nums)):
#     if nums[i] !=val:
#       nums[j]=nums[i]
#       j+=1
#   return j
# print(removeElement([0,1,2,2,3,0,4,2],2))


# Question 2
# Link - https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:
# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# def indeces(haystack,needle):
#   for i in range(len(haystack)):
#     if haystack[i] in needle:
#       return i
#     else:
#       return -1
# print(indeces("leetcode","leeto"))    



# def indeces(haystack,needle):
#   if needle in haystack:
#     return haystack.index(needle)
#   else:
#     return -1
# print(indeces("leetcode","leeto")) 


# Question 3
# Link - https://leetcode.com/problems/longest-common-prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"   

# def prefix(strs):
#   pre=strs[0]
#   length=len(pre)
#   for word in strs[1:]:
#     while pre != word[0:length]:
#       length-=1
#       if length==0:
#         return ""
#       pre=pre[0:length]
#   return pre  
# print(prefix(["flower","flow","flight"])) 

# def prefix(strs):
#   for ch in strs[1]:
#     for i in range(len(ch)):
#       if ch in strs[i]:
#         return ch
#       else:
#         return ""
# print(prefix(["flower","flow","flight"]))      
# lst=["flower","flow","flight"]
# ch=""
# ch +=lst[0][0]
# if ch in lst:
#   print(ch)


# Question 4
# Link - https://leetcode.com/problems/length-of-last-word/description/
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# def length(s):
#   return len(s.split()[-1])
# print(length("   fly me   to   the moon  "))  
# lst=["Hello , World"]
# for ch in lst:
#   print(ch[-1])
# lst=["hy , hello"]
# ch=""
# for word in lst:
#   ch +=word
# print(ch)  
# print(len(lst[-1]))

# def safe_update(db, user, key, new_val):
#   try:
#     db[user][key]=new_val
#   except KeyError:
#     db[user]={}
#     db[user][key]=new_val    
#   return db
# db={}  
# print(safe_update(db,"Deepak","role","admin"))  


# def length(s):
#   for lst in s.strip():
#     print((lst[-1]))
# print(length("Hello World"))

# s=["Hello World"]
# s=str(s).strip().split()
# print(len(s[-1]))
# s=["luffy is still joyboy"]
# for chat in s:
#   chat=chat.split()
#   print(len(chat[-1]))



# Question 5
# Link - https://leetcode.com/problems/merge-sorted-array/

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# def max_profit(prices):
#   i=0
#   j=i+1
#   max_profits=0
#   while i<len(prices) and j<len(prices):
#     if prices[i]>prices[j]:
#       prices[i]=prices[j]
#       j+=1
#       continue
#     else:
#       profit=prices[j]-prices[i]
#       max_profits=max(profit,max_profits)
#       j+=1
#   return max_profits
# print(max_profit([7,1,5,3,6,4]))




# Question 2
# Link - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii


# Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# def remove(nums):
#   if len(nums) <= 2:
#     return len(nums)
#   k = 2  
#   for i in range(2, len(nums)):
#     if nums[i] != nums[k-2]:
#       nums[k] = nums[i]
#       k += 1
#   return k
# print(remove([1,1,1,2,2,3]))

# def remove(nums):
#   res={}
#   for num in nums:
#     res[num]=res.get(num,0)+1
#   for key,value in list(res.items()):
#     if res[value]<2:
#        nums.pop(key)
#   k=len(nums)     
#   return k ,nums  
# print(remove([1,1,1,2,2,3]))
# def remove(nums):
#   i=0
#   j=0
#   count=0
#   while i<len(nums):
#     count +=1
#     if nums[i].count==2:
#       nums[j]=nums[i]
#       j+=1 
#       i+=1  
#     else:
#       del nums[i]
#     i+=1
#     j+=1
#   return nums
# print(remove([1,1,1,2,2,3]))
# def remove(nums):
#   k=2
#   for i in range(2,len(nums)):
#     if nums[i] != nums[k-2]:
#       nums[k]=nums[i]
#       k+=1
#   return k
# print(remove([1,1,1,2,2,3]))

# Question 3
# Link - https://leetcode.com/problems/rotate-array/
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# def rotate(nums, k):
#     n = len(nums)
#     if n == 0:
#         return
#     k = k % n 
#     if k == 0: 
#         return
#     def reverse(arr, start, end):
#         while start < end:
#             arr[start], arr[end] = arr[end], arr[start]
#             start += 1
#             end -= 1
#     reverse(nums, 0, n - 1)
#     reverse(nums, 0, k - 1)
#     reverse(nums, k, n - 1)
#     return nums
# print(rotate([1,2,3,4,5,6,7],3))  
# def rotate(nums,k):
#   return nums[-k:]+nums[:-k]
# print(rotate([-1,-100,3,99],2))
# def rotate(nums,k):
#   k=k%len(nums)
#   l=k-1
#   i=0
#   j=len(nums)-1
#   while i<j:
#     temp=nums[i]
#     nums[i]=nums[j]
#     nums[j]=temp
#     i+=1
#     j-=1
#   j=len(nums)-1 
#   while k<j:
#     temp=nums[k]
#     nums[k]=nums[j]
#     nums[j]=temp
#     k+=1
#     j-=1
#   i=0  
#   while i<l:
#     temp=nums[i]
#     nums[i]=nums[l]
#     nums[l]=temp
#     i+=1
#     l-=1  
#   return nums  
# print(rotate([1,2,3,4,5,6,7],3))





# Question 4
# Link - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
# Find and return the maximum profit you can achieve.
# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

# def max_profit(prices):
#   total_profit = 0
#   for i in range(1, len(prices)):
#     if prices[i] > prices[i-1]:
#       total_profit += prices[i] - prices[i-1]
#   return total_profit
# print(max_profit([7,1,5,3,6,4])) 
# def profit(prices):
#   i=0
#   j=i+1
#   max_profit=0
#   while i<len(prices) and j<len(prices):
#     if prices[i]>prices[j]:
#       i+=1
#       continue
#     else:
#       profit=prices[j]-prices[i]
#       max_profit=max(profit,max_profit)
#     j+=1  
#   return max_profit
# print(profit([7,6,5,4,3,2]))

# def profit(prices):
#   i=0
#   j=i+1
#   max_profit=0
#   sum=0
#   while i<len(prices) and j<len(prices):
#     if prices[i]>prices[j]:
#       i+=1
#       j+=1
#       continue
#     else:
#       profit=prices[j]-prices[i]
#       max_profit=max(profit,max_profit)
#       sum+=profit  
#       j+=1
#     i+=1  
#   return sum
# print(profit([7,6,4,3,1]))


# Question 5
# Link - https://leetcode.com/problems/jump-game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# def jump(nums):
#   max_jump=0
#   for i in range(len(nums)):
#     if nums[i]>nums[i+1]:
      
#   return
# print(jump([2,3,1,1,4]))






# def jump(nums):
#   n = len(nums)
#   if n == 0:
#     return False
#   if n == 1:
#     return True
#   max_reach = 0 
#   for i in range(n):
#     if i > max_reach:
#       return False
#     max_reach = max(max_reach, i + nums[i])
#     if max_reach >= n - 1:
#       return True
#   return False 
# print(jump([2,3,1,1,4]))



# Question 1
# Link - https://leetcode.com/problems/reverse-words-in-a-string
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
# Example 1:
# Input: s = "the sky is blue"
# Output: "blue is sky the"
# def rev(s):
#   s=s.split()
#   return " ".join(s[::-1])
# print(rev("the sky is blue"))


# Question 2
# Link - https://leetcode.com/problems/trapping-rain-water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# Example 1:Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

# Question 3
# Link - https://leetcode.com/problems/candy
# There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# Return the minimum number of candies you need to have to distribute the candies to the children.
# Example 1:
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.



# Question 4
# Link - https://leetcode.com/problems/defanging-an-ip-address
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# def IP(address):
  # add=""
  # for i in address:
  #   if i=='.':
  #     add +='['+'.'+']'
  #     continue
  #   add+=i
  # return add
# print(IP("1.1.1.1"))


  # a = address.replace('.','[.]')
  # return a


# Question 5
# Link - https://leetcode.com/problems/maximum-number-of-words-found-in-sentences
# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# You are given an array of strings sentences, where each sentences[i] represents a single sentence.
# Return the maximum number of words that appear in a single sentence.
# Example 1:
# Input: sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
# Output: 6

# def maxnumber(sentences):
  # i=0
  # max_length=0
  # while i<len(sentence):
  #   length=len(sentence[i].split())
  #   max_length=max(length,max_length)
  #   i+=1 
  # return max_length 
# print(maxnumber(["please wait", "continue to fight", "continue to win"]))
# def maxnumber(sentences):
#    max_length=0
#    for sentence in sentences:
#       max_length=max(max_length,len(sentence.split()))
#    return max_length 
# print(maxnumber(["please wait", "continue to fight", "continue to win"])) 


print(';leey')