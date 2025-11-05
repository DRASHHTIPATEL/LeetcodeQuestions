class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        rots=k%n
        for _ in range(0,rots):
            e=nums.pop()
            nums.insert(0,e)