class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        p = dummy = ListNode(-1)
        carry = 0
        while l1 or l2 or carry:
            val = (l1 and l1.val or 0) + (l2 and l2.val or 0) + carry
            carry = val//10
            p.next = ListNode(val%10)
            l1 = l1 and l1.next
            l2 = l2 and l2.next
            p = p.next
        return dummy.next

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    a = Solution()
    l = a.addTwoNumbers(l1,l2)
    while(l):
        print(l.val)
        l = l.next


