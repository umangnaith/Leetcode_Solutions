class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #st=set(nums)
        #if len(st)==len(nums):return False
        #else:return True
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False 
            