"""Given a sorted singly linked list, remove any duplicates so that no value appears more than once."""

def DedupSortedList(s_l_list):
    # Check if the list is empty
    if s_l_list.head is None:
        return

    # Set parent to the head of the list
    parent = s_l_list.head

    # Set child to the second node in the list
    child = s_l_list.head.next

    # Iterate through the list until child reaches the end
    while child != None:
        # If the child node's value is less than or equal to the parent node's value,
        # it's a duplicate and needs to be removed
        if child.value <= parent.value:
            # Update parent.next to skip the duplicate node
            parent.next = child.next
        else:
            # If child's value is greater than parent's value, move parent to the next node
            parent = parent.next

        # In both cases, move child to the next node
        child = child.next



"""From here on, there is a previous implementation of a linked list and test cases for the previous function."""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBack(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Test case 1: A sorted singly linked list with duplicates
linked_list1 = SinglyLinkedList()
linked_list1.insertAtBack(1)
linked_list1.insertAtBack(2)
linked_list1.insertAtBack(2)
linked_list1.insertAtBack(3)
linked_list1.insertAtBack(4)
linked_list1.insertAtBack(4)
linked_list1.insertAtBack(4)
linked_list1.insertAtBack(5)

print("Before deduplication:")
linked_list1.print_list()

DedupSortedList(linked_list1)
print("After deduplication:")
linked_list1.print_list()
# linked_list1 should now be 1 -> 2 -> 3 -> 4 -> 5

# Test case 2: A sorted singly linked list without duplicates
linked_list2 = SinglyLinkedList()
linked_list2.insertAtBack(1)
linked_list2.insertAtBack(2)
linked_list2.insertAtBack(3)
linked_list2.insertAtBack(4)
linked_list2.insertAtBack(5)

print("Before deduplication:")
linked_list2.print_list()

DedupSortedList(linked_list2)
print("After deduplication:")
linked_list2.print_list()
# linked_list2 should remain unchanged: 1 -> 2 -> 3 -> 4 -> 5
