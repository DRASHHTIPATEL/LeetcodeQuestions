class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # remove duplicates
        n = len(nums)

        # Bubble sort (ascending)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        # If there are fewer than 3 distinct elements
        if n < 3:
            return nums[-1]  # maximum
        else:
            return nums[-3]  # third maximum
