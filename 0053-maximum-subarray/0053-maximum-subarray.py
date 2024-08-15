
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        current_sum = 0
        max_sum = nums[0]
        
        for item in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += item
            max_sum = max(max_sum, current_sum)
        
        return max_sum


        