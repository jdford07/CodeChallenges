import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from LinkedListsLib import LinkedListsLib as linkedList

numList1 = linkedList.createSinglyLinkedList([9, 4, 5, 1])
numList2 = linkedList.createSinglyLinkedList([9, 3, 6])

numList1FollowUp = linkedList.createSinglyLinkedList([4, 9, 9, 9])
numList2FollowUp = linkedList.createSinglyLinkedList([2, 9, 9, 9])


def solution(numList1, numList2):
    carry = False
    numResult = None
    num1 = numList1.head
    num2 = numList2.head

    while num1:
        # Need to reset numResult value to 0 so might as well handle carrying the 1 at the same time
        # If the carry was True for the numList1.tail, we would append node.data = 1 to numList1.tail
        if carry:
            numResult = 1
            carry = False
        else:
            numResult = 0

        numResult += num1.data + num2.data

        if numResult > 9:
            carry = True
            numResult %= 10

        # Store result of place addition in each numList1 node.data
        num1.data = numResult
        num1 = num1.next

        # In the case numList2 is less nodes than numList1
        # Instead of adding more nodes, we set the final numList2 node.data to 0 and continually use it
        if num2.next:
            num2 = num2.next
        else:
            num2.data = 0

    return numList1


def followUpSolution(numList1, numList2):
    numResult = None
    num1 = numList1.head
    num2 = numList2.head

    # First iteration to perform addition without carrying any 1's
    while num1:
        numResult = 0

        numResult += num1.data + num2.data
        # Store result of place addition in each numList1 node.data
        num1.data = numResult
        num1 = num1.next

        # In the case numList2 is less nodes than numList1
        # Instead of adding more nodes, we set the final numList2 node.data to 0 and continually use it
        if num2.next:
            num2 = num2.next
        else:
            num2.data = 0

    # Second iteration to perform carrying of any 1's and storing of final returned node value
    # If the head required a carry, we would append a new node with a 1 to the head of the numList1
    num1 = numList1.head

    while num1:
        if num1.next and num1.next.data > 9:
            num1.data += 1

        num1.data %= 10

        num1 = num1.next

    return numList1


answer = solution(numList1, numList2)
answerFollowUp = followUpSolution(numList1FollowUp, numList2FollowUp)
print(answer)
print(answerFollowUp)
