def linear_search(arr, target):
    # Your code here
    # loop through each value in the array (n)
    for i in range(len(arr)):
        # if the target matches the value
        if arr[i] == target:
            # return the value's index
            return i
    # otherwise return false
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here

    # keep track up lower limit index
    lower = 0
    # keep track of upper limit index
    upper = len(arr) - 1

    # while the higher limit is not equal to the lower limit
    while upper > lower:
        # find the middle (log2(n))
        middle = upper // 2
        # if the target is the value
        if arr[middle] == target:
            # return the index (middle)
            return middle
        # elif the target is less than the value
        elif target < arr[middle]:
            # make the upper limit the middle (if it were middle - 1 you could miss values when you floor divide at the beginning)
            upper = middle
        # else the target is greater than the value
        else:
            lower = middle + 1
    
    # if the while loop ends and you never find the value it isn't there so:
    return -1  # not found
