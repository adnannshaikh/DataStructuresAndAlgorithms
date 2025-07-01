class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            # new_node.prev = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length +=1

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.prev = new_node
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
        next_node = current_node.next

        new_node.next = next_node
        new_node.prev = current_node
        current_node.next = new_node
        if next_node:
            next_node.prev = new_node
        self.length +=1



    def remove(self,index):
        if index < 0 or index >= self.length:
            print("Index is out of range")
            return
        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.length -= 1
            return
        else:
            i = 0
            current_node = self.head
            while i < index-1:
                current_node = current_node.next
                i+=1
            next_node = current_node.next
            current_node.next = next_node.next
            if next_node.next:
                next_node.next.prev = current_node
            self.length -= 1


        # print('cr',current_node)

    def output(self):
        a = []
        current_node = self.head
        while current_node != None:
            a.append(current_node.data)
            current_node = current_node.next
        return a



ll = DoublyLinkedList()
ll.append(33)
ll.append(44)
ll.append(55)
ll.append(66)
ll.insert(2,'x')
ll.remove(2)
print(ll.output())