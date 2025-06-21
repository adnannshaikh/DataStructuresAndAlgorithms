class MyArray {
    constructor(){
        this.length = 0
        this.data = {}
    }

    get(index){
        return this.data[index]
    }

    push(item){
        this.data[this.length] = item;
        this.length++
        return this.length
    }

    pop(){
        const lastItem =  this.data[this.length-1];
        delete this.data[this.length-1]
        this.length--;
        return lastItem
    }

    delete(index){
        const item = this.data[index]
        this.shiftItems(index);
        return item
    }

    shiftItems(index){
        for(let i = index;i< this.length-1;i++){
            this.data[i] = this.data[i+1]
        }
        delete this.data[this.length-1]
        this.length--;
    }
}

const obj = new MyArray();
obj.push(5)
obj.push(7)
obj.push(9)
obj.push(10)
console.log(obj)

// obj.pop()
obj.delete(2)
console.log(obj)