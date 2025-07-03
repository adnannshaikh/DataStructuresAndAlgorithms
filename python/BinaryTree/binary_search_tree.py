class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        else:
            current_node = self.root
            while True:
                if data < current_node.data: # Left
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                elif data > current_node.data: # Right
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right


    def lookup(self,value):
        current_node = self.root
        while True:
            if current_node == None:
                return False
            if current_node.data == value:
                return True
            elif value < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right



    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
        # Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)



tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(20)
tree.insert(1)
tree.insert(6)
tree.insert(15)
tree.insert(170)
tree.print_tree()
print(tree.lookup(9))
