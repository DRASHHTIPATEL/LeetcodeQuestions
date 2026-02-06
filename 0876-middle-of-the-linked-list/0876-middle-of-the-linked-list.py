# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None:
            print("Empty SSL")
        else:
            curr=head
            count=1
            prevnode=curr
            while curr.next is not None:

                
            
                curr=curr.next
                count=count+1

        for i in range(0,count//2):
            prevnode=prevnode.next
        return prevnode

            
