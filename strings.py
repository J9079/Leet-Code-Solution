# Question 1
# Link - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent
# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
# Example 1:
# Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
# Output: true
# def same(word1,word2):
#   str1=""
#   str2=""
#   for i in word1:
#     str1+=i
#   for j in word2:
#     str2+=j
#   if str1==str2:
#     return True
#   else:
#     return False    
# print(same(["ab", "c"],["a", "bc"]))  
  

# Question 2
# Link - https://leetcode.com/problems/number-of-senior-citizens
# You are given a 0-indexed array of strings details. Each element of details provides information about a given passenger compressed into a string of length 15. The system is such that:
# The first ten characters consist of the phone number of passengers.
# The next character denotes the gender of the person.
# The following two characters are used to indicate the age of the person.
# The last two characters determine the seat allotted to that person.
# Return the number of passengers who are strictly more than 60 years old.
# Example 1:
# Input: details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# Output: 2
# def above(details):
#   count=0
#   for detail in details:
#     if detail[11:13]>str(60):
#       count+=1
#   return count
# print(above(["7868190130M7522","5303914400F9211","9273338290F4010"])) 

 
# Question 3
# Link - https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage
# You are given a 0-indexed array of strings garbage where garbage[i] represents the assortment of garbage at the ith house. garbage[i] consists only of the characters 'M', 'P' and 'G' representing one unit of metal, paper and glass garbage respectively. Picking up one unit of any type of garbage takes 1 minute.
# You are also given a 0-indexed integer array travel where travel[i] is the number of minutes needed to go from house i to house i + 1.
# There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0 and must visit each house in order; however, they do not need to visit every house.
# Only one garbage truck may be used at any given moment. While one truck is driving or picking up garbage, the other two trucks cannot do anything.
# Return the minimum number of minutes needed to pick up all the garbage.
# Example 1:
# Input: garbage = ["G","P","GP","GG"], travel = [2,4,3]
# Output: 21
# def pick(garbage,travel):
#   g=""
#   total=0
#   for i in range(len(garbage)-1):
#     g+=garbage[i]
#     for gar in garbage:  
#       if g in gar:
#         total+=1
#         print(gar)
#   return total
# print(pick(["G","P","GP","GG"],[2,4,3]))  
# def pick(garbage,travel):
# def pick(garbage, travel):
#     for i in range(1, len(travel)):
#         travel[i] += travel[i - 1]
#     total = 0
#     for house in garbage:
#         total += len(house)
#     last_M = -1
#     last_P = -1
#     last_G = -1
#     for i in range(len(garbage)):
#         if 'M' in garbage[i]:
#             last_M = i
#         if 'P' in garbage[i]:
#             last_P = i
#         if 'G' in garbage[i]:
#             last_G = i
#     if last_M > 0:
#         total += travel[last_M - 1]
#     if last_P > 0:
#         total += travel[last_P - 1]
#     if last_G > 0:
#         total += travel[last_G - 1]
#     return total
# print(pick(["G","P","GP","GG"],[2,4,3]))    

# Question 4
# Link - https://leetcode.com/problems/find-and-replace-pattern
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
# Example 1:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# def encode(s):
#   mapping={}
#   result=[]
#   count=0
#   for ch in s:
#     if ch not in mapping:
#       mapping[ch]=count
#       count+=1
#     result.append(mapping[ch])  
#   return result
# def matching(words,pattern):
#   same_word=encode(pattern)
#   return [word for word in words if encode(word)==same_word]
# print(matching(["abc","deq","mee","aqq","dkd","ccc"],"abb"))
# def matching(words,pattern):
#   result=[]
#   for word in words:
#     pattern_word={}
#     word_pattern={}
#     match=True
#     for p,w in zip(pattern,word):
#       if p in pattern_word:
#         if pattern_word[p]!=w:
#           match=False
#           break
#       else:
#         pattern_word[p]=w
        
#       if w in word_pattern:
#         if word_pattern[w]!=p:
#           match=False
#           break
#       else:
#         word_pattern[w]=p
#     if match:
#       result.append(word)  
#   return result
# print(matching(["abc","deq","mee","aqq","dkd","ccc"],"abb"))
# def matching(words,pattern):
#   res={}
#   result=[]
#   i=0
#   for s in pattern:
#     if s in res:
#       result.append(res[s])
#     else:
#       i+=1
#       res[s]=i
#       result.append(i) 
#   p=matching(pattern)    
#   result=[]
#   for word in words:
#     if matching(word)==p:
#       result.append(word)     
#   return result
# pattern="abb"
# words=["abc","deq","mee","aqq","dkd","ccc"]


# def convert_to_indices(words,text):
#     text = text.lower()
  
#     patt= ''.join(str(ord(char) - ord('a')) for char in text )
#     word= ''.join(str(ord(w) - ord('a')) for word1 in words for w in word1 )
#     if word == patt:
#       print(words) 
# print(convert_to_indices(["abc","deq","mee","aqq","dkd","ccc"],"abb"))

# Question 5
# Link - https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target
# Given an array of digit strings nums and a digit string target, return the number of pairs of indices (i, j) (where i != j) such that the concatenation of nums[i] + nums[j] equals target.
# Example 1:
# Input: nums = ["777","7","77","77"], target = "7777"
# Output: 4


# def equals(nums,target):
#   count=0
#   for i in range(len(nums)):
#     for j in range(len(nums)-1,-1,-1):
#         if nums[i]+nums[j]==target:
#           if i !=j:
#              count+=1
#   return count      
# print(equals(["777","7","77","77"],"77"))




# Question 6
# Link - https://leetcode.com/problems/valid-number
# Given a string s, return whether s is a valid number.
# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".
# Formally, a valid number is defined using one of the following definitions:
# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.
# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.
# The digits are defined as one or more digits.
# Example 1:
# Input: s = "0"
# Output: true
# def isNumber(s):
#   digit_seen = False
#   dot_seen = False
#   exponent_seen = False
#   digit_exponent = True
#   for i, ch in enumerate(s):
#     if ch.isdigit():
#         digit_seen = True
#         if exponent_seen:
#             digit_exponent = True
#     elif ch == ".":
#         if dot_seen or exponent_seen:
#             return False
#         dot_seen = True
#     elif ch == "e" or ch == "E":
#         if exponent_seen or not digit_seen:
#             return False
#         exponent_seen = True
#         digit_exponent = False
#     elif ch == "+" or ch == "-":
#         if i != 0 and s[i - 1] not in "eE":
#             return False
#     else:
#         return False
#   return digit_seen and digit_exponent
# print(isNumber("0"))

# votes =[101,102,101,102,101,101,102]
# for i in votes:
#   if i//2 == votes:
#     print(votes)