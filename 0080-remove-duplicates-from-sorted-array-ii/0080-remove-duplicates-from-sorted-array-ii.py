class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index=1
        num=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1] and num<2:
                nums[index]=nums[i]
                num+=1
                index+=1
            elif nums[i]!=nums[i-1]:
                nums[index]=nums[i]
                num=1
                index+=1
            i+=1
        return index


        