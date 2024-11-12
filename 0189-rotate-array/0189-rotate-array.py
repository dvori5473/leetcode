class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Handle cases where k is greater than n
        nums[:] = nums[-k:] + nums[:-k]  # Rotate using slicing
                


        