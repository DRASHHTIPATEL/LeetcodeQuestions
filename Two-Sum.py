class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# we created a dict to store nums seen so far from the array
        preMap={}#val: index
# we find diff for eacy and then check if its in our hashmap .. return index of it and index of the current
        for i,n in enumerate(nums):
            diff=target-n
            if diff in preMap:
                return[preMap[diff],i]
            preMap[n]=i
            
        return
        