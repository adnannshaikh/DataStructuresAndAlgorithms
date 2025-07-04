class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Queues:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self,data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length+=1

    def dequeue(self):
        dq = self.first
        self.first = self.first.next
        return dq

    def show(self):
        current_node = self.first
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


qe = Queues()
qe.enqueue(88)
qe.enqueue(8)
qe.enqueue(9)
qe.enqueue(0)
qe.enqueue(1)
qe.show()
print("-----------")
qe.dequeue()
qe.dequeue()
qe.dequeue()
qe.show()