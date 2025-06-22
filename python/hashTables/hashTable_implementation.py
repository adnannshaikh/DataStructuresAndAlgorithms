class HashTable:
    def __init__(self):
        self.data = []

    def __hash(key):
        hash  = 0
        for i in range(len(key)):
            hash = (hash +key.ord(i) * 1) % len(self.data))
        return hash
    
    def set(k,v):
        
