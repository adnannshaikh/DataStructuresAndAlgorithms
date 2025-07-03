class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
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
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return "Queueu is empty"
        dq = self.first
        self.first = self.first.next
        self.length -= 1
        return dq.data

    def peek(self):
        return self.first.data

    def show(self):
        current_node = self.first
        # i = 0
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

q = Queue()

q.enqueue(8)
q.enqueue(78)
q.enqueue(6)
q.enqueue("fried")
q.show()
print("-----------")
q.dequeue()
q.dequeue()
q.show()
