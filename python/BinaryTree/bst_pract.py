class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Bst:
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
                if data < current_node.data:
                    if current_node.left is None:
                        current_node.left = new_node
                        return
                    else:
                        current_node = current_node.left
                elif data > current_node.data:
                    if current_node.right is None:
                        current_node.right = new_node
                        return
                    else:
                        current_node = current_node.right

    def lookup(self,data):
        current_node = self.root
        while True:
            if current_node is None:
                return False
            if current_node.data == data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

    def remove(self,data):
        current_node = self.root
        while True:
            if data == current_node.data:
                del_node = current_node
                current_node.right = current_node.right.right
                return
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
            #TBC....




    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
        # Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)


tr = Bst()
tr.insert(33)
tr.insert(90)
tr.insert(2)
tr.insert(3)
tr.print_tree()
print(tr.lookup(90))
tr.remove(3)