class Array:
    def __init__(self):
        self.length = 0
        self.data = {}
    def showAll(self):
        li = [self.data[i] for i in range(0,self.length)]
        return li
    def get(self,index):
        return self.data[index]

    def push(self,value):
        self.data[self.length] = value
        self.length+=1

    def pop(self):
        item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return item


arr1 = Array()
arr1.push(10)
arr1.push(22)
arr1.push(3)
arr1.push(56)
arr1.push(7)
print(arr1.showAll())
it = arr1.pop()
print(arr1.showAll())
print(it)