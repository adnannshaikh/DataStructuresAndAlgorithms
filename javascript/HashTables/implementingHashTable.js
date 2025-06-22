class HashTable{
    constructor(size){
        this.data = new Array(size);
    }

    _hash(key){
    let hash = 0
    for(let i = 0;i<key.length;i++){
        hash = (hash + key.charCodeAt(i) * 1) % this.data.length
    }
    return hash;
    }

    set(key,value){
        let address = this._hash(key)
        if(!this.data[address]){
            this.data[address] = [];
            this.data[address].push([key,value])
            console.log(this.data)
        }else{
            this.data[address].push([key,value])
            return this.data
        }
    }

    get(key){
        let address = this._hash(key)
        const currentBucket = this.data[address]
        if(currentBucket){
            for(let i = 0;i<currentBucket.length;i++){
                if(currentBucket[i][0]===key){
                    return currentBucket[i][1]
                }
            }
        }
        return undefined
    }
}





const ht = new HashTable(50);
ht.set('grapes',10000);
ht.set('grapes','ramu')
ht.set('oranges',10000);
console.log(ht.get('grapes'))