'''
Xiaochi Ma
2018-11-06
'''

def missingWords(s, t):
    
    if len(s) == 0:
        return []
    if len(t) == 0:
        return s.split(" ")
    
    list1 = s.split(" ")
    org = set(list1)
    target = set(t.split(" "))
    
    org -= target
    
    res = []
    for word in list1:
        if word in org:
            res.append(word)
    
    return res

if __name__ == '__main__':
    print(missingWords("I am using HackerRank to improve programming", "am HackerRank to improve"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    