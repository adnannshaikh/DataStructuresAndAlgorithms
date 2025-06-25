class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length +=1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length +=1

    def insert(self,index,data):
        new_node = Node(data)
        if index == 0:
            self.prepend(new_node)
        if index >= self.length:
            self.append(new_node)
        else:
            current_node = self.head
            i = 0
            while i<index-1:
                current_node = current_node.next
                i+=1
            new_node.next = current_node.next
            current_node.next = new_node
            self.length+=1

    def remove(self,index):
        if index < 0 or index >= self.length:
            print("Index out of range")
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        i = 0
        current_node = self.head
        while i<index-1:
            current_node = current_node.next
            i+=1
        current_node.next = current_node.next.next
        self.length -=1

    def pr(self):
        i = self.head
        a = []
        while i is not None:
            a.append(i.data)
            i = i.next
        return a



li = LinkedList2()
li.append(9)
li.append(33)
li.append(44)
li.append(0)
li.prepend(34)
li.insert(3,88)
# print(li.length)
print(li.pr())
li.remove(2)
print(li.pr())


