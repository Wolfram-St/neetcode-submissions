class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indexed = sorted((val, idx) for idx, val in enumerate(nums))
        left, right = 0, len(indexed) - 1
        while left < right:
            s = indexed[left][0] + indexed[right][0]
            if s > target:
                right -= 1
            elif s < target:
                left += 1
            else:
                i, j = indexed[left][1], indexed[right][1]
                return [min(i, j), max(i, j)]
        return []