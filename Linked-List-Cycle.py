1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        
10        slow=head
11        fast=head
12        while fast is not None and fast.next is not None:
13            slow=slow.next
14            fast=fast.next.next
15            if slow==fast:
16                return True
17        return False