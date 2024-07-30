
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LIFO - Last in First Out
# Stack class contains 1 field: top
# top is a Node
# When referencing a specific node, you access top.data and top.next
class Stack:
    def __init__(self, data=None):
        if(data):
            self.top = Node(data)
        else:
            self.top = None
    
    def push(self, data):
        newNode = Node(data)
        
        if self.top:
            newNode.next = self.top
            self.top = newNode 
        else:
            self.top = newNode
    
    def pop(self):
        if self.top:
            self.top = self.top.next
        else:
            raise Exception(f"Stack [{self}] is Empty")
    
    def peek(self):
        if self.top:
            return self.top
        else:
            raise Exception(f"Stack [{self}] is Empty")

    def isEmpty(self):
        return self.top == None

# FIFO - First in First Out
# Queue has 2 fields, first: head node of the list, last: tail node of the list
class Queue:
    def __init__(self, data=None):
        if(data):
            self.first = Node(data)
            self.last = Node(data)
        else:
            self.first = None
            self.last = None
        
    # Add a new node to the tail, set first & last appropriately
    def add(self, data):
        newNode = Node(data)
        
        # Because we set last to None in remove(), we know if there's a last node then there is a first node
        # Conversely, if there is no last node, then we must set the first node
        if self.last:
            self.last.next = newNode
            self.last = newNode
        else:
            self.first = newNode
            self.last = newNode
            
    # Remove the first item from the list
    def remove(self):
        if self.first:
            self.first = self.first.next
            
            # When removing, if the fist node is None then there are no nodes left
            # Therefor we set last to None
            if not self.first:
                self.last = self.first
        else:
            raise Exception(f"Queue [{self}] is Empty")
    
    # Return the first node 
    def peek(self):
        if self.first:
            return self.first
        else:
            raise Exception(f"Queue [{self}] is Empty")
    
    # Returns a bool of True or False
    def isEmpty(self):
        return self == None