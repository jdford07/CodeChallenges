import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from LinkedListsLib import LinkedListsLib as linkedList

singlyLinkedList = linkedList.createSinglyLinkedList([1, 12, 2, 4, 7, 3, 4, 5, 6, 7])
kthToLast = 8


def solution(input, kthToLast):
    currentNode = input.head
    listNodeCount = 0

    while currentNode:
        listNodeCount += 1
        currentNode = currentNode.next

    returnIndex = listNodeCount - kthToLast

    if returnIndex <= 0:
        return None
    else:
        i = 1
        currentNode = input.head

        while returnIndex != i:
            currentNode = currentNode.next
            i += 1

    return currentNode


def bookSolutionRecursive(currentNode, k):
    if not currentNode:
        return -1

    index = bookSolutionRecursive(currentNode.next, k) + 1

    if k == index:
        print(f"kth to last element is: {currentNode.data}")

    return index


def bookSolutionIterative(singlyLinkedList, k):
    p1 = singlyLinkedList.head
    p2 = singlyLinkedList.head

    # Place p1 at Kth position of linked list
    for i in range(k):
        if p1.next != None:
            p1 = p1.next

    # Iterate until the end of the linked list, p2 should be at the kth from last spot
    while p1.next:
        p1 = p1.next
        p2 = p2.next

    return p2


answer = solution(singlyLinkedList, kthToLast)
bookRecursive = bookSolutionRecursive(singlyLinkedList.head, kthToLast)
bookIterative = bookSolutionIterative(singlyLinkedList, kthToLast)
print(answer)
print(bookRecursive)
print(bookIterative)
