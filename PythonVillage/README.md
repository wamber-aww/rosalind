# Introduction

This is the **Introductory Exercises** from [Rosalind](http://rosalind.info/problems/topics/introductory-exercises/). 
This part contains six basic python questions

# Questions

## Q1: Installing Python
  - After downloading and installing Python, type `import this` into the Python command line and see what happens. 
Then, click the "Download dataset" button below and copy the Zen of Python into the space provided.

## Q2: Variables and Some Arithmetic

  - Given: Two positive integers a and b, each less than 1000.  
  - Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

**Sample Dataset**
```
3 5
```
**Sample Output**
```
34
```

## Q3: Strings and Lists

  - Given: A string s of length at most 200 letters and four integers a, b, c and d.
  - Return: The slice of this string from indices a through b and c through d (with space in between), 
inclusively. In other words, we should include elements s[b] and s[d] in our slice.

**Sample Dataset**
```
HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.  
22 27 97 102
```
**Sample Output**
```
Humpty Dumpty
```

## Q4: Conditions and Loops

  - Given: Two positive integers a and b (a<b<10000).
  - Return: The sum of all odd integers from a through b, inclusively.

**Sample Dataset**
```
100 200
```
**Sample Output**
```
7500
```


## Q5: Working with Files

  - Given: A file containing at most 1000 lines.
  - Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

**Sample Dataset**
```
Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat
```
**Sample Output**
```
Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat
```

## Q6: Intro to Python dictionary

  - Given: A string s of length at most 10000 letters.
  - Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

**Sample Dataset**
```
We tried list and we tried dicts also we tried Zen
```
**Sample Output**
```
and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
```
