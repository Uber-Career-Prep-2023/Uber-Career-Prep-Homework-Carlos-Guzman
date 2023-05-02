"""Given a singly linked list, move the nth from the last element to the front of the list.
"""

def MoveNthLastToFront(k, s_l_list):
    list_len = s_l_list.length() 
    # Initialize parent and child pointers
    parent = s_l_list.head
    child = s_l_list.head.next
    
    # If k is larger than the length of the list, return the list unchanged or the list has only one node, return the list unchanged
    if k > list_len or child == None:
        return s_l_list
    
    
    # Calculate the number of iterations needed to reach the desired node
    iterate = list_len - k -1
    
    # Iterate through the list to find the parent node of the target node
    for i in range(iterate):
        parent = child
        child = parent.next
        
    # Reassign the pointers to move the target node to the front of the list
    aux = child
    parent.next = child.next
    aux.next = s_l_list.head
    s_l_list.head = aux

        

"""From here on, there is a previous implementation of a single linked list and test cases for the previous function."""


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
    def length(self): # Function to calculate the length of the linked list
        length = 0  
        current = self.head  
        while current != None:  
            length += 1  
            current = current.next  
        return length  
    
# Creating a singly linked list
singly_list = SinglyLinkedList()
singly_list.insertAtBack(1)
singly_list.insertAtBack(2)
singly_list.insertAtBack(3)
singly_list.insertAtBack(4)
singly_list.insertAtBack(5)

# Moving the 2nd last element to the front
MoveNthLastToFront(2, singly_list)
# Resulting list should be: 4 -> 1 -> 2 -> 3 -> 5

# Moving the last element to the front
MoveNthLastToFront(1, singly_list)
# Resulting list should be: 5 -> 4 -> 1 -> 2 -> 3

# Moving the 3rd last element to the front
MoveNthLastToFront(3, singly_list)
# Resulting list should be: 1 -> 5 -> 4 -> 2 -> 3

