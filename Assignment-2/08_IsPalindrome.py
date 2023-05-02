"""Given a doubly linked list, determine if it is a palindrome"""
def IsPalindrome(double_list):
    # Initialize two pointers: one at the start and one at the end of the list
    left_pointer = double_list.head
    right_pointer = double_list.last
    
    # Iterate through the list until left_pointer and right_pointer meet at the middle
    while left_pointer != right_pointer:
        # If the data in the left_pointer node is not equal to the data in the right_pointer node, the list is not a palindrome, so return False
        if left_pointer.data != right_pointer.data:
            return False
        
        # Move left_pointer to the next node in the list
        left_pointer = left_pointer.next
        # Move right_pointer to the previous node in the list
        right_pointer = right_pointer.prev
    
    # If the while loop completes without returning False, the list is a palindrome, so return True
    return True



"""From here on, there is a previous implementation of a double linked list and test cases for the previous function."""




class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def insertAtFront(self, value=None):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.last = new_node
            return self.head
        aux = self.head
        self.head = new_node
        new_node.next = aux
        aux.prev = new_node
        return self.head

    def insertAtBack(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.last = new_node
            return self.last
        aux = self.last
        self.last = new_node
        aux.next = self.last
        self.last.prev = aux
        return self.last


def print_linked_list(linked_list):
    current = linked_list.head
    while current is not None:
        print(current.data, end=' -> ')
        current = current.next
    print("None")
# Test cases for IsPalindrome function
double_list1 = SinglyLinkedList()
double_list1.insertAtBack('a')
double_list1.insertAtBack('b')
double_list1.insertAtBack('c')
double_list1.insertAtBack('b')
double_list1.insertAtBack('a')
print_linked_list(double_list1)
print(IsPalindrome(double_list1))  # Output should be True

double_list2 = SinglyLinkedList()
double_list2.insertAtBack('a')
double_list2.insertAtBack('b')
double_list2.insertAtBack('c')
double_list2.insertAtBack('d')


print_linked_list(double_list2)
print(IsPalindrome(double_list2))  # Output should be False

double_list3 = SinglyLinkedList()
double_list3.insertAtBack('a')
double_list3.insertAtBack('b')
double_list3.insertAtBack('b')
double_list3.insertAtBack('a')

print_linked_list(double_list3)
print(IsPalindrome(double_list3))  # Output should be True

double_list4 = SinglyLinkedList()
double_list4.insertAtBack('a')

print_linked_list(double_list4)
print(IsPalindrome(double_list4))  # Output should be True

