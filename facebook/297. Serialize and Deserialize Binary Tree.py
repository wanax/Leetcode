'''
Xiaochi Ma
2018-11-01
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Codec:

    def serialize(self, root):

        def rserialize(root, string):
            """ a recursive helper function for the serialize() function."""
            # check base case
            if root is None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = rserialize(root.left, string)
                string = rserialize(root.right, string)
            return string
        
        return rserialize(root, '')
    
    def deserialize(self, data):
        
        def rdeserialize(l):
            """ a recursive helper function for deserialization."""
            if l[0] == 'None':
                l.pop(0)
                return None
                
            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root
    
if __name__ == '__main__':
    
        root = TreeNode(1)
        node1 = TreeNode(2)
        node2 = TreeNode(3)
        node3 = TreeNode(4)
        node4 = TreeNode(5)
        
        root.left = node1
        root.right = node2
        
        node2.left = node3
        node2.right = node4
    
        codec = Codec()
#        codec.deserialize(codec.serialize(root))
        
        node = codec.deserialize(codec.serialize(root))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        