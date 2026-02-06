1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8#(o(1) sc and o(1) tc =optimum sol)
9        if head is None or head.next is None:
10            return head
11        odd=head
12        even=head.next
13        even_head=even
14        while even is not None and even.next is not None:
15            odd.next=odd.next.next
16            odd=odd.next
17            even.next=even.next.next
18            even=even.next
19
20
21        odd.next=even_head
22        return head
23        
24
25        