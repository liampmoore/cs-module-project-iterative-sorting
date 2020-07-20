# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    # n complexity
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        # n - i complexity, loop through cur_index to the end of the array
        for j in range(i + 1, len(arr)):
            # if the arr[j] is smaller than the smallest then arr[j] is the smallest
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    # keep track of index with the last sorted item decrementing from the last index of the array
    sorted = len(arr)
    # start looping (n) until sorted index is zero (falsey)
    while sorted:
        # iterate from the first item in the array all the way up until the last sorted item (n - i)
        for i in range(0, sorted - 1):
            # if the current item is greater than the next item switch them
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        # decrement the last sorted item index
        sorted -= 1
    return arr

'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here

    if len(arr) == 0:
        return arr

    # if there is no specified maximum you add (n) complexity to find the maximum
    if maximum is None:
        maximum = 0
        for value in arr:
            if value < 0:
                return "Error, negative numbers not allowed in Count Sort"
            if value > maximum:
                maximum = value

    # create an array of zeros with a length equal to the maximum value plus 1 (to account for zero)
    buckets = [0] * (maximum + 1)

    # loop through the original arr (n) and increment values in buckets
    for value in arr:
            if value < 0:
                return "Error, negative numbers not allowed in Count Sort"
            buckets[value] += 1
    
    # for the purpose of creating the new array, keep track of the currently selected possible value in the array of possible values
    current_value = 0
    # keep track of the index of the original array as you loop through it
    array_index = 0

    # while the current index is less than the len of the original array (n + max)
    while array_index < len(arr):
        # if the currently selected value bucket has zero values:
        if buckets[current_value] == 0:
            current_value += 1
        # else
        else:
            # decrement the bucket of the currently selected value
            buckets[current_value] -= 1
            # add the value to the current index of the original array
            arr[array_index] = current_value
            # increment the current index of the array
            array_index += 1
    
    return arr

# total is O(n + max) time complexity with 0(n + max) space complexity