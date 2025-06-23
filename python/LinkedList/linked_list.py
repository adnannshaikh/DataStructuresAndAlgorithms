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

    def printLL(self):
        i = self.head
        a = []
        while i is not None:
            a.append(str(i.data))
            i = i.next
        return '->'.join(a)



li = LinkedList()
li.append(10)
li.append(16)
li.prepend(66)
li.append(11)
print(li.printLL())