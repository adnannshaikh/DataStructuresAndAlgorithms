class Stack:
    def __init__(self):
        self.data = []
        self.length = 0

    def push(self,data):
        self.data.append(data)
        self.length += 1
        return

    def pop(self):
        self.length -=1
        return self.data.pop()

    def peek(self):
        return self.data[self.length-1]

    def show(self):
        i = self.length
        while i > 0:
            print(self.data[i-1])
            i -= 1

stc = Stack()
stc.push(8)
stc.push(90)
stc.push(55)
stc.show()
stc.pop()
print("-----------")
stc.show()