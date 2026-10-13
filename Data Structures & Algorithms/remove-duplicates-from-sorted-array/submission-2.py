class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        left = 1

        for right in range(len(nums)):
            if nums[right] != nums[left - 1]:
                nums[left] = nums[right]
                left += 1

        return left
        