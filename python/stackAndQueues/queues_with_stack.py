class Queue:
    def __init__(self):
        self.first = []
        self.last = []

    def enqueue(self,data):
        while self.first:
            self.last.append(self.first.pop)

        self.last.append(data)
        return

    def dequeue(self):
        if not self.first:
            while self.last:
                self.first.append(self.last.pop())
        if self.first:
            return self.first.pop()
        return "Queue is empty"

    def peek(self):
        if self.first:
            return self.first[-1]
        elif self.last:
            return self.last[0]
        return None

    def show(self):
        queue = self.first[::-1] + self.last
        print("Queue (Front to Back):", queue)

stq = Queue()
stq.enqueue(99)
stq.enqueue(88)
stq.enqueue(77)
stq.dequeue()
stq.show()
