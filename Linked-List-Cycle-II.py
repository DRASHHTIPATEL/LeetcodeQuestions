1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
9        slow=head
10        fast=head
11        while fast is not None and fast.next is not None:
12            slow=slow.next
13            fast=fast.next.next
14            if slow==fast:
15                slow=head
16                while slow!=fast:
17                    slow=slow.next
18                    fast=fast.next
19                return slow
20
21        