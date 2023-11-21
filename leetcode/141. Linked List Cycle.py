#If there is a cycle, when you move have two different head that move the list one time and two times, they will eventually meet.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s,f = head,head
        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s:
                return True
        return False
