'''
Xiaochi Ma
2018-11-06
'''

def missingWords2(s, t):
    
    s = s.strip()
    t = t.strip()
    
    if len(s) == 0:
        return []
    if len(t) == 0:
        return s.split(" ")
    
    list1 = s.split(" ")
    list2 = t.split(" ")
    
    dic1 = {}
    for word in list1:
        dic1[word] = dic1.get(word, 0) + 1
    
    dic2 = {}
    for word in list2:
        dic2[word] = dic2.get(word, 0) + 1

    for key, value in dic2.items():
        dic1[key] -= value
    
    res = []
    for word in list1:
        if dic1[word] > 0:
            res.append(word)
    
    return res

def missingWords(s, t):
    
    s = s.strip()
    t = t.strip()
    
    ss = s.split(" ")
    tt = t.split(" ")
    
    res = []
    i, j = 0, 0
    while i < len(ss) and j < len(tt):
        if ss[i] != tt[j]:
           res.append(ss[i])
        else:
            j += 1
        i += 1
    
    while i < len(ss):
        res.append(ss[i])
        i += 1
    
    return res

if __name__ == '__main__':
    print(missingWords("I am using HackerRank to improve programming", "am HackerRank to improve"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    