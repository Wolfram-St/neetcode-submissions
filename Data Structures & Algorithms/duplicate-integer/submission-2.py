class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        right = 1
        left = 0

        while right < len(nums):
            if nums[left] == nums[right]:
                return True
            
            right+=1
            left+=1
        return False

            


