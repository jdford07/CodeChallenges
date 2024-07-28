import sys
import math
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from LinkedListsLib import LinkedListsLib as linkedList

list1 = linkedList.createSinglyLinkedList([3, 3, 3, 3])
list2 = linkedList.createSinglyLinkedList([9, 9, 9])
list3 = linkedList.createSinglyLinkedList([0, 1, 2])

linkedList.appendListToListTail(list1, list3)
linkedList.appendListToListTail(list2, list3)


class intersectingNode:
    def __init__(self, list1Node, list2Node, intersectNode, intersectBool):
        self.list1Node = list1Node
        self.list2Node = list2Node
        self.intersectNode = intersectNode
        self.intersectBool = intersectBool


# Find the length of the passed in Linked List
def findListLength(numList):
    currentNode = numList
    count = 0

    while currentNode:
        currentNode = currentNode.next
        count += 1

    return count


# Insert X amount of 0's to the head of the passed in Linked List
def padListHead(numList, padding):
    head = numList

    for i in range(padding):
        head = insertNodeAtHead(head, 0)

    return head


def insertNodeAtHead(list, data):
    listHead = list
    newNode = linkedList.createNode(data)

    if listHead != None:
        newNode.next = listHead

    return newNode


def compareNodes(list1, list2, intersectNode, intersectBool):
    if not list1 and not list2:
        newNode = intersectingNode(list1, list2, None, False)
        return newNode

    compare = compareNodes(list1.next, list2.next, intersectNode, intersectBool)

    if compare.list1Node == compare.list2Node:
        compare.intersectBool = True
        compare.intersectNode = compare.list1Node

    compare.list1Node = list1
    compare.list2Node = list2

    return compare


def solution(list1, list2):
    list1Length = findListLength(list1)
    list2Length = findListLength(list2)

    if list1Length < list2Length:
        padding = list2Length - list1Length
        list1 = padListHead(list1, padding)
    else:
        padding = list1Length - list2Length
        list2 = padListHead(list2, padding)

    intersection = compareNodes(list1, list2, None, False)

    if intersection.intersectBool:
        return intersection.intersectNode
    else:
        return intersection.intersectBool


answer = solution(list1.head, list2.head)
print(answer)
