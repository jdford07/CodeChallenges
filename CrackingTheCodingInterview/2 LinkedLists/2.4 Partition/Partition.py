import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from LinkedListsLib import LinkedListsLib as linkedList

singlyLinkedList = linkedList.createSinglyLinkedList([ 8, 3, 2, 3, 1, 13, 9 , 7, 5, 4, 8, 12])
partitionValue = 4


def solution(input, partitionValue):
    listLength = 0
    tailNode = input.head
    currentNode = input.head
    prevNode = None
    
    # Find last node of the list
    while tailNode.next:
        tailNode = tailNode.next
        listLength += 1
    
    # Instantiate and use a listLength count to avoid an infinite loop 
    for i in range(listLength+1):
        if(currentNode.data >= partitionValue):
            tailNode.next = currentNode
            
            if(prevNode):
                prevNode.next = currentNode.next
            else:
                input.head = currentNode.next
            
            currentNode = currentNode.next
            tailNode = tailNode.next
            tailNode.next = None
            
            # move node to tail
        else:
            prevNode = currentNode
            currentNode = currentNode.next
            
    return input


answer = solution(singlyLinkedList, partitionValue)
print(answer)
