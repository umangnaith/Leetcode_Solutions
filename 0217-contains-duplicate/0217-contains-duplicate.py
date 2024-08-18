class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        st=set(nums)
        if len(st)==len(nums):return False
        else:return True
        