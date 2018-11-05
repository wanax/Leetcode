'''
Xiaochi Ma
2018-11-02
'''
import collections

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word):
        
        node = self.root
        for c in word:
            node = node.children[c]
        node.isWord = True

    def search(self, word):
        
        res = self.find(self.root, word)
        return False if res == False else True
    
    def find(self, node, word):
        
        if not word:
            if node.isWord:
                return True
        if word[0] == '.':
            for n in node.children.values():
                self.find(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return False
            self.find(node, word[1:])
    
    
if __name__ == '__main__':
    
    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("mad")
    print(obj.search("pad"))
    print(obj.search("bad"))
    print(obj.search(".ad"))
    print(obj.search("b.."))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    