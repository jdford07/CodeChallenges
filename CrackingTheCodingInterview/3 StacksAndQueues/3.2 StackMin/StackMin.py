import sys
import math
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from StackQueueLib import StackQueueLib as stackQueue

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackWithMin:
    def __init__(self, data=None):
        if(data):
            newNode = Node(data)
            self.top = newNode
            self.min = [newNode]
        else:
            self.top = None
            self.min = []
    
    def push(self, data):
        newNode = Node(data)
        
        if self.top:
            newNode.next = self.top
            self.top = newNode 
        else:
            self.top = newNode
        
        if(len(self.min) > 0):
            if(self.top.data < self.min[0].data):
                self.min.insert(0, self.top)
        else:
            self.min.insert(0, self.top)
    
    def pop(self):
        if self.top:
            if(self.top == self.min[0]):
                self.min.pop(0)
            self.top = self.top.next
        else:
            raise Exception(f"Stack [{self}] is Empty")
    
    def peek(self):
        if self.top:
            return self.top
        else:
            raise Exception(f"Stack [{self}] is Empty")
    
    def min(self):
        if self.top:
            return self.min.top
        else:
            raise Exception(f"Stack [{self}] is Empty")

    def isEmpty(self):
        return self.top == None

def solution(input):

    return input

stack = StackWithMin(None)
stack.push(20)
stack.push(25)
stack.push(5)
stack.pop()
stack.pop()


answer = solution(inputArr)
print(answer)
