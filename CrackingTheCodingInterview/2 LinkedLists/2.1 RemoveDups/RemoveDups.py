import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from LinkedListsLib import LinkedListsLib as linkedList

singlyLinkedList = linkedList.createSinglyLinkedList([1, 2, 2, 4, 7, 3, 4, 5, 6, 7])


def solution(input):
    uniqueChar = set()
    currentNode = input.head
    prevNode = None

    while currentNode:
        if currentNode.data in uniqueChar:
            prevNode.next = currentNode.next
        else:
            uniqueChar.add(currentNode.data)
            prevNode = currentNode

        currentNode = currentNode.next

    return input


answer = solution(singlyLinkedList)
print(answer)
