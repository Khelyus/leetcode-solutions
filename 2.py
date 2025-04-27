'''You are given two non-empty linked lists representing
two non-negative integers.
The digits are stored in reverse order,
and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        digits1 = []
        while l1:
            digits1.append(l1.val)
            l1 = l1.next
        number1 = int("".join(map(str, reversed(digits1))))

        digits2 = []
        while l2:
            digits2.append(l2.val)
            l2 = l2.next
        number2 = int("".join(map(str, reversed(digits2))))

        total = number1 + number2
        sum_str = str(total)

        dummy = ListNode(0)
        current = dummy

        for digit in reversed(sum_str):
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next