1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
8        dummy = ListNode(0)
9        dummy.next = head
10        slow=dummy
11        fast=head
12        while fast is not None:
13            if fast.val == val:
14                slow.next = fast.next      # remove fast
15            else:
16                slow = slow.next           # keep fast, move slow forward
17            fast = fast.next               # always move fast
18
19        return dummy.next