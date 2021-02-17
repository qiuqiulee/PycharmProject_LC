class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def rearrangeLastN(l, n):
    head = fast = slow = l
    for _ in range(n):
        fast = fast.next
    print(fast)
    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = l

    return l

print(rearrangeLastN([1,2,3,4,5],3))