class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.bottom = None
        self.top = None
        self.length = 0

    def push(self,data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def peek(self):
        if self.top is None:
            return "No Element inside"
        return f"peak is : {self.top.data}"

    def pop(self):
        if self.top == self.bottom:
            self.top = None
        current_node = self.top
        self.top = current_node.next
        self.length -= 1
        return current_node.data

    def isEmpty(self):
        if self.top is None:
            print("Empty Stack")
        else:
            return print(False)

    def search(self,data):
        length = self.length
        while True:
            if data == self.top.data:
                return print(f"index at {length-1}")
            else:
                self.top = self.top.next
                length -= 1



    def show(self):
        current_node = self.top
        a = []
        while current_node is not None:
            a.append(current_node.data)
            current_node = current_node.next

        for i in a:
            print(i)


s = Stack()
s.push(9)
s.push(7)
s.push(2)
s.push(4)
s.push(5)
s.push(77)
s.show()
# s.pop()
# s.show()
# print(s.peek())
# s.isEmpty()
s.search(77)