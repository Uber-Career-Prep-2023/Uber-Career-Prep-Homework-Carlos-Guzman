class Node:
    def __init__(self, data):
        self.data = data
        self.next = None   # Pointer to the next node in the list

class SinglyLinkedList:
    def __init__(self):
        self.head = None   # Pointer to the first node in the list
        self.last = None   # Pointer to the last node in the list
        
    def insertAtFront(self, value): #creates new Node with data val at front; returns new head
        # Create a new node with the specified value
        new_node = Node(value)
        
        if self.head == None:   # If the list is empty
            self.head = new_node   # Set the new node as both the first and last node
            self.last = new_node
            return self.head
        
        # If the list is not empty, set the new node as the first node and update the head pointer
        aux = self.head
        self.head = new_node
        new_node.next = aux   # Set the next pointer of the new node to the old first node
        return self.head
    
    def insertAtBack(self, value): #creates new Node with data val at end
        # Create a new node with the specified value
        new_node = Node(value)
        
        if self.head == None:   # If the list is empty
            self.head = new_node   # Set the new node as both the first and last node
            self.last = new_node
            return self.last   # Return the last node
        
        # If the list is not empty, set the new node as the last node and update the last pointer
        aux = self.last
        self.last = new_node
        aux.next = self.last   # Set the next pointer of the previous last node to the new last node
        return self.last

    def insertAfter(self, head, value, loc): #creates new Node with data val after Node loc
        # Create a new node with the specified value
        new_node = Node(value)

        # Set a pointer to the head node
        current = head

        # Traverse the linked list until reaching the node after which the new node should be inserted
        while current != loc:
            current = current.next

        # Set the next pointer of the new node to the node after the current node
        new_node.next = current.next

        # Set the next pointer of the current node to the new node
        current.next = new_node

        # Return a reference to the newly inserted node
        return new_node
    def deleteFront(self, head):   # Definition of the `deleteFront` function that takes the head of the list as a parameter
        self.head = head.next   # Update the head of the list to point to the second node
        del head   # Free the memory occupied by the first node
        return self.head   # Return the new updated head of the list

    def deleteBack(self, head):  # Function to delete the last node in a linked list

        current = head  # Set 'current' to the head of the list

        while current.next != None:  # Traverse until the last node
            aux = current  
            current = current.next

        # At this point, 'current' is the last node, and 'aux' is the second-to-last node

        self.last = aux  # Update the 'last' property to the second-to-last node
        self.last.next = None  # Set the new last node's 'next' pointer to 'None'

        del current  # Delete the last node

        return self.last  # Return the updated last node of the list

    def deleteNode(self,head, loc): #deletes Node loc; returns head
        if loc == head: #if the node to be deleted is the head node deletes the head node and returns None
            del head
            return None
        # Set a pointer to the head node
        current = head
        # Traverse the linked list until reaching the node after which the new node should be inserted
        while current != loc:
            aux = current
            current = current.next
        # Set the next pointer of the previus node to the nex node of loc
        aux.next = current.next
        del current
        # Return a reference to the previus node
        return aux
    def length(head): # Function to calculate the length of the linked list
        length = 0  # Initialize a variable to keep track of the length
        current = head  # Set a pointer to the head of the linked list
        while current != None:  # Traverse the linked list until the end
            length += 1  # Increment the length variable for each node in the list
            current = current.next  # Move to the next node in the list
        return length  # Return the length of the linked list

    def reverseIterative(self,head): #reverses the linked list iteratively
        current = head  # Set a pointer to the head of the linked list
        stack = [] # Create an empty stack to store the data of each node in the linked list.
        while current != None: #Traverse the linked list using a while loop and append the data of each node to the stack.
            stack.append(current.data) 
            current = current.next
        linked_list_reversed = SinglyLinkedList() #Create a new linked list linked_list_reversed using the SinglyLinkedList class.
        for i in reversed(stack): #Iterate over the stack in reverse order using a for loop.
            linked_list_reversed.insertAtFront(i) # Insert each item from the stack into the linked_list_reversed using the insertAtFront method of the SinglyLinkedList class.
        return linked_list_reversed #Return the reversed linked list.
            


    """def reverseRecursive(head):   #reverses the linked list recursively
        current =  head
        if current.next == None:
            return current
        else:
            current = head.next 
            reverseRecursive(current) 
    """

# Create an empty linked list
my_list = SinglyLinkedList()

# Insert a node with value 1,2 and 3 at the front of the list
my_list.insertAtFront(1)
my_list.insertAtFront(2)
my_list.insertAtFront(3)
# Insert a node with value 5,6 and 7 at the back of the list
my_list.insertAtBack(5)
my_list.insertAtBack(6)
my_list.insertAtBack(7)
# Insert a node with value 4 after the node with value 2
my_node = my_list.head
while my_node.data != 2:
    my_node = my_node.next
my_list.insertAfter(my_list.head, 4, my_node)

# Print the list
my_node = my_list.head
print('linked list:')
while my_node != None:
    print(my_node.data)
    my_node = my_node.next
# Delete the first node of the list
my_list.deleteFront(my_list.head)
# Delete the last node of the list
my_list.deleteBack(my_list.head)
# Print the list
# Delete the node with value 4 from the list
my_node = my_list.head
while my_node.data != 4:
    my_node = my_node.next
my_list.deleteNode(my_list.head, my_node)

# Print the list
print('linked list deleting elements')
my_node = my_list.head
while my_node != None:
    print(my_node.data)
    my_node = my_node.next
print("Length of the linked list:", my_list.length(my_list.head))
# Reverse the linked list
reversed_list = my_list.reverseIterative(my_list.head)

# Print the reversed list
my_node = reversed_list.head
while my_node != None:
    print(my_node.data)
    my_node = my_node.next


""" 
Node insertAtFront(Node head, int val) // creates new Node with data val at front; returns new head
void insertAtBack(Node head int val) // creates new Node with data val at end
void insertAfter(Node head, int val, Node loc) // creates new Node with data val after Node loc
Node deleteFront(Node head) // removes first Node; returns new head
void deleteBack(Node head) // removes last Node
Node deleteNode(Node head, Node loc) // deletes Node loc; returns head
int length(Node head) // returns length of the list
Node reverseIterative(Node head) // reverses the linked list iteratively
Node reverseRecursive(Node head) // reverses the linked list recursively (Hint: you will need a helper function)
"""


