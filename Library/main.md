### _*Printing a certain amount of decimal values*_
    print("%.6f"%value)

### _*First and last four elements*_
    arr[:4]
    arr[-4:]

### _*Count elements from a list to a dictionary*_
    from collections import Counter
    arrayDict = dict(Counter(array))


### _*Signed Integer to Unsigned Integer*_
    unsigned = signed + (1 << 32)

### _*To add value to each element in a list*_
    array = [i+value  for i in array]

### _*Left and right Diagonal of a 2D square array*_
    left = [arr[i][i] for i in range(size)]
    right = [arr[i][size-i-1] for i in range(size)]

### _*A square (might bepossible on normal 2D arrays) matrix reveresed by column and rows, The elements possible on a position are*_
    matrix[i][j],
    matrix[i][length-j],
    matrix[length-i][j],
    matrix[length-i][length-j]

### _*Empty array initialization difference*_
#### _*Without Referencing*_
    arr = [[] for i in range(3)]
    arr[0].append(2)

##### *Result*
    [[2],[],[]]

#### *With Referencing*
    arr = [[]*3]
    arr[0].append(2)

##### *Result*
    [[2],[2],[2]]

#### *Explanation*
 In " []*3 ", all the empty list references the same list. That's y if an list is updated then all the lists are updated.
 In " [] for i in range(3) ", all the empty list doesn't point at a single point.

#### *Stack Overflow*
[Appending to 2D lists in Python [duplicate]](https://stackoverflow.com/questions/7745562/appending-to-2d-lists-in-python)

### _**_