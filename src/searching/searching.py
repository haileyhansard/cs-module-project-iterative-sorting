def linear_search(arr, target):
    #Your code here
    for i in range(0, len(arr)):
        if (arr[i] == target):
            return i;
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # find the midpoint element
    # length // 2
    # keep track of the left and right most points
    left = 0
    right = len(arr) - 1 #because len(arr) is not a valid index, since arr indexes start at 0. it would be 0-9 indexes, but len would be 10. so we do 10 - 1 = 9.

    #keep iterating so long as left <= right
    while left <= right:
        midpoint = (right + left) //2

        if arr[midpoint] == target:
            return midpoint

        elif arr[midpoint] > target:
            #toss out the left side of the array
            #toss out the midpoint element itself as well
            right = midpoint - 1
        else: 
            left = midpoint + 1
    #otherwise, we didn't find what we're looking for

    return -1  # not found
