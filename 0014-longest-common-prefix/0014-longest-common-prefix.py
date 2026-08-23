class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre=strs[0]
        length=len(pre)
        for word in strs[1:]:
          while pre != word[0:length]:
            length-=1
            if length==0:
              return ""
            pre=pre[0:length]
        return pre 