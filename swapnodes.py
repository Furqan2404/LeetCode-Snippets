from typing import Optional
class LinkedList():
    def  __init__(self, val=0, next=None):
        self.val= val
        self.next = next

class Solution :
    def swappairs(self, head:Optional[LinkedList])->Optional[LinkedList]:
        dummy = LinkedList(0,head)
        prev , curr = dummy , head
        while curr and curr.next:
            nxtpair = curr.next.next
            secondnode = curr.next

            secondnode.next = curr 
            curr.next = nxtpair
            prev = curr
            curr = nxtpair

        return dummy.next
