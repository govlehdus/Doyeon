#having a right pointer that check whether it is the end or not. If it is the last element and there is a n space between the right and left, so simply make left.next = left.next.next.
#Use dummy node to handle the edge cases.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = dummy
        second =  head

        while n >0:
            second = second.next
            n-=1

        while second:
            first = first.next
            second = second.next

        first.next = first.next.next
        return dummy.next
