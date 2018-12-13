'''
Xiaochi Ma
2018-12-07
'''
class Node(object):
    def __init__(self, val):
        self.val = val
        self.count = 0
        self.child = {}
        self.isWord = False

class Trie(object):

    def __init__(self):
        self.root = Node(0)
        
    def ins(self, word, root):
        
        node = None
        if word[0] in root.child:
            node = root.child[word[0]]
        else:
            node = Node(word[0])
            root.child[word[0]] = node
        
        if len(word) == 1:
            node.isWord = True
            return
        else:
            self.ins(word[1:], node)
            
    
    def insert(self, word):
        self.ins(word, self.root)
        

    def search(self, word):
        
        i = 0
        node = self.root
        while i < len(word):
            if word[i] in node.child:
                node = node.child[word[i]]
                i += 1
            else:
                return False
        if node.isWord:
            return True
        return False
        

    def startsWith(self, prefix):
        i = 0
        node = self.root
        while i < len(prefix):
            if prefix[i] in node.child:
                node = node.child[prefix[i]]
                i += 1
            else:
                return False
        return True
        

if __name__ == '__main__':
    obj = Trie()
    obj.insert("abca")
    print(obj.search("aba"))
    print(obj.startsWith("a"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    