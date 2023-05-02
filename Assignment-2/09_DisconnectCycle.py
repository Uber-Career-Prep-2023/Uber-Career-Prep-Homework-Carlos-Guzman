"""Given a singly linked list, disconnect the cycle, if one exists."""
#I was not able to solve this one :( i dont have any idea how to do it 
def detectCycle(head):
    slow = head
    fast = head.next

    while slow and fast:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next

    """if not slow or not fast:
        return None

    slow = head
    while slow != fast:
        slow = slow.next

    slow.next = None
    """
    return head