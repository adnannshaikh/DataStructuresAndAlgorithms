class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

        self.bottom = None
        self.length = 0


    def peek(self):
        print(f"peak : {self.top.data}")

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.bottom =  new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1


    def pop(self):
        if self.top == self.bottom:
            self.top = None
        hp = self.top
        self.top = self.top.next
        return hp.data


    def isEmpty(self):
        if self.bottom is None:
            return True
        else:
            return False


    def show(self):
        i = 0
        current_node = self.top
        a = []
        while current_node is not None:
            a.append(current_node.data)
            i += 1
            current_node = current_node.next

        for i in a:
            print(i)



stc = Stack()
stc.push(99)
stc.push(79)
stc.push(98)
stc.push(88)
stc.push(4)
stc.show()
stc.pop()
stc.pop()
print("---------------")
stc.show()
