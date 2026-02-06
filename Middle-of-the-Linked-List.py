1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
8
9        if head is None:
10            print("Empty SSL")
11        else:
12            curr=head
13            count=1
14            prevnode=curr
15            while curr.next is not None:
16
17                
18            
19                curr=curr.next
20                count=count+1
21
22        for i in range(0,count//2):
23            prevnode=prevnode.next
24        return prevnode
25
26            
27