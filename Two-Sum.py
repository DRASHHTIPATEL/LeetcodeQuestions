class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hash={}
        for i in range(0,n):
            remaining=target-nums[i]
            if remaining in hash:
                return [hash[remaining],i]
            hash[nums[i]]=i