class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'
class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for i in range(1, len(tree_data)):
            BinarySearchTree.addNode(self.root, TreeNode(tree_data[i]))
    def data(self):
        return self.root
    def sorted_data(self):
        return BinarySearchTree.traverse(self.root)
        
    def addNode(root, node):
        if int(node.data) > int(root.data):
            if root.right == None:
                root.right = node
            else:
                BinarySearchTree.addNode(root.right, node)
        else:
            if root.left == None:
                root.left = node
            else:
                BinarySearchTree.addNode(root.left, node)
                
        
    def traverse(root):
        array = [root.data]
        
        if root.left != None:
            array = BinarySearchTree.traverse(root.left) + array
        if root.right != None:
            array = array + BinarySearchTree.traverse(root.right)
        return array