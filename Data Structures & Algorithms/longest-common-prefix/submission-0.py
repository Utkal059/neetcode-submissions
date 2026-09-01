class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i,c in enumerate(zip(*strs)):
            if len(set(c))>1: return strs[0][:i]
        return min(strs,key=len)