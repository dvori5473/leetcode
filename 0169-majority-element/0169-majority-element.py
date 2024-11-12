class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        k=len(nums)
        n=nums[k//2]
        return n
        