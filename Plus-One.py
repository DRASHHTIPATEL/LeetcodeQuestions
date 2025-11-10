class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        num=0
        for x in digits:
            num=num*10+x
        num+=1
        digits = [int(d) for d in str(num)]
        return digits
       
    

