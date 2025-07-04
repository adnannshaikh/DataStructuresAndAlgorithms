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
        popped =  self.data.pop()
        return popped

    def show(self):
        i = self.length
        while i > 0:
            print(self.data[i-1])
            i-=1
sa = Stack()
sa.push(0)
sa.push(4)
sa.push(7)
sa.push(88)
sa.push(56)
sa.show()
sa.pop()
print("------------------")
sa.show()