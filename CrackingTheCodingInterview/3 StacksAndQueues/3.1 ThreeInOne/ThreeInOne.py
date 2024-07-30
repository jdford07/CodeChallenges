import sys
import math
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from StackQueueLib import StackQueueLib as stackQueue

stack1 = stackQueue.Stack()
stack2 = stackQueue.Stack()
stack3 = stackQueue.Stack()

inputArr = [1,2,3,4,5,6,7,8,9]

def solution(input):
    arrLen = len(input)
    for i in range(arrLen):
        if(i == 0 or i < round(arrLen/3)):
            stack1.push(input[i])
        elif(i == round(arrLen/3) or i < round(arrLen*2/3)):
            stack2.push(input[i])
        elif(i<= round(arrLen)):
            stack3.push(input[i])
        

    return input
answer = solution(inputArr)
print(answer)
