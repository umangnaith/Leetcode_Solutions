class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lon,cur=1,1
        nums_ls=list(sorted(set(nums)))
        i=0
        if len(nums_ls) == 0: return 0
        while i < len(nums_ls)-1:
            if abs(nums_ls[i+1]-nums_ls[i]) == 1:
                cur += 1
                lon = max(cur,lon)
            else:
                 cur = 1
            i += 1
        return(lon)