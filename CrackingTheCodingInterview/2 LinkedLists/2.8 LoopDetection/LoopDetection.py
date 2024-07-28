import sys
import math
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from LinkedListsLib import LinkedListsLib as linkedList

list1 = linkedList.createSinglyLinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

list = list1.head
while list:
    tail = list
    list = list.next

loopStartNode = list1.head
while loopStartNode:
    if loopStartNode.data == 10:
        tail.next = loopStartNode
        break
    loopStartNode = loopStartNode.next


def solution(list):
    slow = list
    fast = list

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = list
            break

    # No loop exists
    if not fast or not fast.next:
        return None

    while fast:
        if slow == fast:
            return fast
        slow = slow.next
        fast = fast.next


answer = solution(list1.head)
print(answer)
