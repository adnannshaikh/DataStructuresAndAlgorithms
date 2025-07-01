# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def append(self,data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             self.head = self.tail
#             self.length = 1
#         else:
#             self.tail.next = new_node
#             self.tail = new_node
#             self.length +=1
#
#     def printLL(self):
#         i = self.head
#         while i != None:
#             print(i.value)
#             i = i.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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


    def insert(self,index,data):
        if index >= self.length:
            self.append(data)
            return
        new_node = Node(data)
        if index == 0:
            self.prepend(data)
        else:
            current_node = self.head
            i = 0
            while i<index-1:
                current_node = current_node.next
                i+=1
            new_node.next = current_node.next
            current_node.next = new_node
        self.length +=1

    def remove(self,index):
        if index < 0 or index >= self.length:
            print("Index out of range")
            return

        if index==0:
            self.head = self.head.next
            self.length-=1
            return
        i = 0
        current_node = self.head
        while  i < index-1:
            current_node = current_node.next
            i+=1
        current_node.next = current_node.next.next
        self.length-=1



    def reverse(self):
        prev = None
        # self.tail = self.head
        while self.head != None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = prev


    def printLL(self):
        i = self.head
        a = []
        while i is not None:
            a.append(str(i.data))
            i = i.next
        return '->'.join(a)


ll = LinkedList()
ll.append(90)
ll.append(7)
ll.append(10)
print(ll.printLL())
ll.reverse()
print(ll.printLL())