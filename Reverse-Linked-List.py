1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        temp=head
9        stack=[]
10        while temp is not None:
11            stack.append(temp.val)
12            temp=temp.next
13        temp=head
14        while temp is not None:
15            e=stack.pop()
16            temp.val=e
17            temp=temp.next
18        return head