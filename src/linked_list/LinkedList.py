class Node:    
    def __init__(self, data):        
        self.value = data        
        self.next = None

class LinkedList:
       
    head = Node(None)
    tail = Node(None) 
    
    def __init__(self):
        self.head = self.tail = None
        
    def isEmpty(self):
        return self.head == None
    
    def addLast(self, data):
        node = Node(data)
        if self.isEmpty():
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node
 
    def remove_node(self,target):
        # If the list is empty, return None
        if not self.head:
            return None

        # If the target is the head, update the head pointer
        if self.head.value == target:
            return self.head.next

        # Traverse the list to find the node before the target
        prev = self.head
        current = self.head.next
        while current:
            if current.value == target:
                # Remove the node by updating the pointers
                prev.next = current.next
                return self.head
            prev = current
            current = current.next

        # If the target is not found, return the head
        return self.head
 
    # method to make the list iterable
    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next    
            