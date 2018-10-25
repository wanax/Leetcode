#######################

# Machine Learning Test 2018/10/01
# Miles Ma
#
########################

def changeNode2Num(node):
    
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
    
    num = ''
    for i in nums[::-1]:
        num += str(i)
    num = int(num)
    return num

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
    

if __name__ == '__main__':
    
    node1 = ListNode(2)
    node2 = ListNode(4)
    node3 = ListNode(3)
    
    node1.next = node2
    node2.next = node3
    
    node11 = ListNode(5)
    node22 = ListNode(6)
    node33 = ListNode(4)
    
    node11.next = node22
    node22.next = node33
    
    num1 = changeNode2Num(node1)
    num2 = changeNode2Num(node11)
    
    sumNum = num1 + num2
    sumNum = str(sumNum)
    sumNums = []
    for a in sumNum:
        sumNums.append(a)
       
    head = ListNode(0)
    
    node = ListNode(int(sumNums[-1]))
    head = node
    
    for i in range(len(sumNums) - 2, -1, -1):
        tempNode = ListNode(int(sumNums[i]))
        node.next = tempNode
        node = tempNode

    while head:
        print(head.val)
        head = head.next






























