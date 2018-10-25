#######################

# Machine Learning Test 2018/09/30
# Miles Ma
#
########################

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

dic = {}
def fib2(n):
    dic[1] = 1
    dic[0] = 0
    if(n not in dic):
        dic[n] = fib2(n-1) + fib2(n-2)
    return dic[n]

class PackageItem:
    
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

def getPackage(bagItems, bagSize):
    
    matrix = [[0 for x in range(0, bagSize + 1)] for y in range(len(bagItems))]
    for m in range(1, bagSize + 1):
        for n in range(len(bagItems)):
            item = bagItems[n]
            if item.weight > m: #背包装不下第j个元素
                if n == 0: #开始第一个元素都放不下，置0
                    matrix[n][m] = 0
                else:
                    matrix[n][m] = matrix[n-1][m] #则直接取抛开j元素的最优解
            else:
                newPrice = 0
                if n == 0:
                    matrix[n][m] = item.value #第一个元素， 直接装入
                    continue
                else:
                    newPrice = matrix[n-1][m - item.weight] + item.value
                matrix[n][m] = max(newPrice, matrix[n-1][m])
    
    answers = []
    curSize = bagSize
    for i in range(len(bagItems)-1, -1, -1):
        item = bagItems[i]
        if curSize == 0:
            break
        if i == 0 and curSize > 0:
            answers.append(item.name)
            break
        if matrix[i][curSize] - matrix[i - 1][curSize - item.weight] == item.value:
            answers.append(item.name)
            curSize -= item.weight
            
    return answers
                
    

if __name__ == "__main__":
    
    bagSize = 10
    names = ['a', 'b', 'c', 'd', 'e']
    weights = [2, 2, 6, 5, 4]
    values = [6, 3, 5, 4, 6]
    bagItems = []
    
    for i in range(len(names)):
        item = PackageItem(names[i], weights[i], values[i])
        bagItems.append(item)
    
    print(getPackage(bagItems, bagSize))































