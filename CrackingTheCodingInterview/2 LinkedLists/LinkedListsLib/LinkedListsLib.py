class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, newNode):
        currentNode = self.head

        if currentNode:
            while currentNode.next:
                currentNode = currentNode.next
            currentNode.next = newNode
        else:
            self.head = newNode


def createNode(data):
    return Node(data)


def createSinglyLinkedList(data):
    singlyLinkedList = SinglyLinkedList()

    for item in data:
        singlyLinkedList.append(Node(item))

    return singlyLinkedList
