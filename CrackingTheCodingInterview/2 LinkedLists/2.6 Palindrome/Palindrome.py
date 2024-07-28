import sys
import math
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from LinkedListsLib import LinkedListsLib as linkedList

list = linkedList.createSinglyLinkedList(
    ["a", "b", "b", "c", "d", "d", "c", "b", "b", "a"]
)


class wrapperNode:
    def __init__(self, head, tail, boolResult):
        self.head = head
        self.tail = tail
        self.boolResult = boolResult


def reverseLinkedList(list):
    forwardList = list.head
    reverseList = list.head

    while forwardList:
        newNode = linkedList.createNode(forwardList.data)
        newNode.next = reverseList
        reverseList = newNode
        forwardList = forwardList.next

    return reverseList


def compareNodes(head, tail, result):
    if not tail.next:
        node = wrapperNode(head, tail, True)
        return node

    resultNode = compareNodes(head, tail.next, result)

    if resultNode.boolResult:
        if resultNode.head.data != resultNode.tail.data:
            resultNode.boolResult = False

    resultNode.head = resultNode.head.next
    resultNode.tail = tail
    return resultNode


def solution(list):

    result = compareNodes(list.head, list.head, True)

    return result


answer = solution(list)
reversed = reverseLinkedList(list)
print(answer)
