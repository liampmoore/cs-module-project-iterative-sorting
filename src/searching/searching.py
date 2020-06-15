def linear_search(arr, target):
    # Your code here

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    minimum = 0
    maximum = len(arr) - 1

    while minimum <= maximum:
        middle = (maximum + minimum) // 2
        # if the middle is less than the target get rid of everything less than the middle
        if  arr[middle] < target:
            minimum = middle + 1
        # if the middle is greater than the target get rid of everything greater than the middle
        elif arr[middle] > target:
            maximum = middle - 1
        # if the middle is the target return the index
        else:
            return middle
        
    return -1  # not found
