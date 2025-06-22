'''
Given a list of integers, count how many times each element appears.
'''

def count(arr):
    di = {}
    for i in arr:
        if i in di:
            di[i]+=1
        else:
            di[i] = 1
    return di

'''
2. Find First Non-Repeating Character in a String
Problem:
Given a string, find the first character that does not repeat.

'''

def non_rep_str(str):
    di = {}
    for char in str:
        di[char] = di.get(char,0)+1

    for char in di:
        if di[char]==1:
            return char
''''
3. Check if Two Strings are Anagrams
Problem:
Two strings are anagrams if they contain the same characters with the same frequency. 
Check if two strings are anagrams using a dictionary.
'''

def anagram(str1,str2):
    d1,d2={},{}
    for ch in str1:
        d1[ch] = d1.get(ch,0)+1

    for ch in str2:
        d2[ch] = d2.get(ch,0)+1
    
    return d1==d2
    

'''
4. Find the Most Frequent Element in a List
Problem:
Return the element with the highest frequency in the list
'''

def high_freq(arr):
    di = {}
    max_count = 0
    max_element = None
    for i in arr:
        di[i] = di.get(i,0)+1
        if di[i]>max_count:
            max_count = di[i]
            max_element = i
    return max_element
    # using max and get
    # return max(di,key=di.get)
    # -----------------------------

'''
5. Group Words by Their Length
Problem:
Given a list of words, group them into a dictionary where keys are word lengths and values are lists of words of that length.

Example:

python
Copy
Edit
Input: ["hi", "hello", "world", "to", "a"]
Output: {2: ['hi', 'to'], 5: ['hello', 'world'], 1: ['a']}
'''
def word_count(li):
    di = {}
    for i in li:
        length = len(i)
        if length in di:
            di[length].append(i)
        else:
            di[length] = [i]
    return di
print(word_count(["hi", "hello", "world", "to", "a"]))