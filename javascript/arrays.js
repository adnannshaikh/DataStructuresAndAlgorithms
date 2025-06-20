const str = ['a','b','c','d']

//push
str.push('f') //O(1)

//pop - last element of array is removed
str.pop() //O(1)

//unshift
str.unshift('x') //O(n)

//splice
str.splice(2,0,'alien') //O(n)
console.log(str)


