# Exercise-Tuples-and-Sets---Python-Advanced-


## 1. Unique Usernames

Write a program that reads from the console a sequence of `N` usernames and keeps a collection of only the unique ones. On the first line, you will receive an integer `N`. On the next `N` lines, you will receive a username. Print the collection on the console (the order does not matter).

### Examples:

**Input:**
```
6  
George  
George  
George  
Peter  
George  
NiceGuy1234
```

**Output:**
```
George  
Peter  
NiceGuy1234
```

**Input:**
```
10  
Peter  
Maria  
Peter  
George  
Steve  
Maria  
Alex  
Peter  
Steve  
George
```

**Output:**
```
Peter  
Maria  
George  
Steve  
Alex
```

---

## 2. Sets of Elements

Write a program that prints a set of elements. On the first line, you will receive two numbers - `n` and `m`, separated by a single space - representing the lengths of two separate sets. On the next `n + m` lines, you will receive `n` numbers, which are the numbers in the first set, and `m` numbers, which are in the second set. Find all the unique elements that appear in both and print them on separate lines (the order does not matter).

### Examples:

**Input:**
```
4 3  
1  
3  
5  
7  
3  
4  
5
```

**Output:**
```
3  
5
```

**Input:**
```
2 2  
1  
3  
1  
5
```

**Output:**
```
1  
3
```

---

## 3. Periodic Table

Write a program that keeps all the unique chemical elements. On the first line, you will be given a number `n` - the count of input lines that you will receive. On the following `n` lines, you will be receiving chemical compounds separated by a single space. Your task is to print all the unique ones on separate lines (the order does not matter).

### Examples:

**Input:**
```
4  
Ce O  
Mo O Ce  
Ee  
Mo
```

**Output:**
```
Ce  
Ee  
Mo  
O
```

**Input:**
```
3  
Ge Ch O Ne  
Nb Mo Tc  
O Ne
```

**Output:**
```
Ch  
Ge  
Mo  
Nb  
Ne  
O  
Tc
```

---

## 4. Count Symbols

Write a program that reads a text from the console and counts the occurrences of each character in it. Print the results in alphabetical (lexicographical) order.

### Examples:

**Input:**
```
SoftUni rocks
```

**Output:**
```
 : 1 time/s  
S: 1 time/s  
U: 1 time/s  
c: 1 time/s  
f: 1 time/s  
i: 1 time/s  
k: 1 time/s  
n: 1 time/s  
o: 2 time/s  
r: 1 time/s  
s: 1 time/s  
t: 1 time/s
```

**Input:**
```
Why do you like Python?
```

**Output:**
```
 : 4 time/s  
?: 1 time/s  
P: 1 time/s  
W: 1 time/s  
d: 1 time/s  
e: 1 time/s  
h: 2 time/s  
i: 1 time/s  
k: 1 time/s  
l: 1 time/s  
n: 1 time/s  
o: 3 time/s  
t: 1 time/s  
u: 1 time/s  
y: 3 time/s
```

---

## 5. Longest Intersection

Write a program that finds the longest intersection. You will be given a number `N`. On each of the next `N` lines, you will be given two ranges in the format: "{first_start},{first_end}-{second_start},{second_end}". You should find the intersection of these two ranges. The start and end numbers in the ranges are inclusive.

Finally, find the longest intersection of all `N` intersections. Print the numbers that are included and its length in the format: "Longest intersection is [{longest_intersection_numbers}] with length {length_longest_intersection}".

### Note:

In each range, there will always be an intersection. If there are two equal intersections, print the first one.

### Examples:

**Input:**
```
3  
0,3-1,2  
2,10-3,5  
6,15-3,10
```

**Output:**
```
Longest intersection is [6, 7, 8, 9, 10] with length 5
```

**Comment:**
- The intersection of [0-3] and [1-2] is [1-2] (length 2)  
- The intersection of [2-10] and [3-5] is [3-5] (length 3)  
- The intersection of [6-15] and [3-10] is [6-10] (length 5) - which is the longest

**Input:**
```
5  
0,10-2,5  
3,8-1,7  
1,8-2,4  
4,7-2,5  
1,10-2,11
```

**Output:**
```
Longest intersection is [2, 3, 4, 5, 6, 7, 8, 9, 10] with length 9
```

---

## 6. Battle of Names

You will receive a number `N`. On the following `N` lines, you will be receiving names. You should sum the ASCII values of each letter in the name and integer divide it by the number of the current row (starting from 1). Save the result to a set of either odd or even numbers, depending on if the resulting number is odd or even. After that, sum the values of each set.

- If the sums of the two sets are equal, print the union of the values, separated by ", ".
- If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
- If the sum of the even numbers is bigger than the sum of the odd numbers, print the symmetric-different values, separated by ", ".

### Note:

On every operation, the starting set should be the odd set.

### Examples:

**Input:**
```
4  
Pesho  
Stefan  
Stamat  
Gosho
```

**Output:**
```
304, 128, 206, 511
```

**Comment:**
- The sum of ASCII values for "Pesho" is 511. Integer divide by row (1): 511 / 1 = 511  
- The sum of ASCII values for "Stefan" is 609. Integer divide by row (2): 609 / 2 = 304  
- The sum of ASCII values for "Stamat" is 618. Integer divide by row (3): 618 / 3 = 206  
- The sum of ASCII values for "Gosho" is 512. Integer divide by row (4): 512 / 4 = 128

The odd set: 511  
The even set: 304, 206, 128  
The sum of the even numbers is larger, so print the symmetric-different values.

**Input:**
```
6  
Preslav  
Gosho  
Ivan  
Stamat  
Pesho  
Stefan
```

**Output:**
```
733, 101
```
```
