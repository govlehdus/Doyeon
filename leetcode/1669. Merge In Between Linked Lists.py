# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        first = list1
        second = list1
        for i in range(a-1):
            first = first.next
        for x in range(b+1):
            second = second.next
        first.next = list2
        temp = list2
        while temp.next != None:
            temp = temp.next
        temp.next = second
        return list1
