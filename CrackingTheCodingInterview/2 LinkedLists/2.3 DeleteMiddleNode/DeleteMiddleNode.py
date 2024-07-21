import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from LinkedListsLib import LinkedListsLib as linkedList

singlyLinkedList = linkedList.createSinglyLinkedList([ 1, 2, 3, 4, 5, 6, 7, 8])
removeItem = 8

def solution(input, removeItem):
    listHead = input.head
    currentNode = input.head
    removeNode = None
    prevNode = None
    
    # Find where node to remove is
    while currentNode:
        if(currentNode.data == removeItem):
            removeNode = currentNode
            break
        else:
            currentNode = currentNode.next
            
    # Conditional to make sure:
    # 1. Node to remove is not the start of list
    # 2. Node to remove is not null
    # 3. Node to remove is not the end of list 
    if(listHead != removeNode and removeNode and removeNode.next):
        while removeNode.next:
            removeNode.data = removeNode.next.data
            prevNode = removeNode
            removeNode = removeNode.next

        # When the final node is found, the prevNode will be final node - 1
        # Remove the final node from the list 
        prevNode.next = None
    else:
        return False
        
    return True


answer = solution(singlyLinkedList, removeItem)
print(answer)
