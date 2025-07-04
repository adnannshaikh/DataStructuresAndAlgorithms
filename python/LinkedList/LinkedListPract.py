class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
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
            self.prepend(data)
            return
        if index >= self.length:
            self.append(data)
            return
        i = 0
        current_node = self.head
        while i < index-1:
            current_node = current_node.next
            i+=1
        new_node.next = current_node.next
        current_node.next = new_node
        print("Cr", current_node.data)
        self.length +=1



    def remove(self,index):
        if index < 0 or index >= self.length:
            print("Index is out of range")
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            i = 0
            current_node = self.head
            while i < index-1:
                current_node = current_node.next
                i+=1
            current_node.next = current_node.next.next
            self.length -= 1


        # print('cr',current_node)

    def output(self):
        a = []
        current_node = self.head
        while current_node != None:
            a.append(current_node.data)
            current_node = current_node.next
        return a



ll = LinkedList()
ll.append(33)
ll.append(53)
ll.append(89)
ll.append(99)
ll.prepend('k')
ll.prepend(25)
ll.insert(4,77)
ll.remove(2)
print(ll.output())