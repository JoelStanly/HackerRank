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

### _**_