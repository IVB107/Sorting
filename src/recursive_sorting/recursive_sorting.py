# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    merged_arr = []

    l, r = 0, 0
    while l < len(arrA) and r < len(arrB):

        if arrA[l] < arrB[r]:
            merged_arr.append(arrA[l])
            l += 1
        elif arrB[r] < arrA[l]:
            merged_arr.append(arrB[r])
            r += 1

    while r < len(arrB):
        merged_arr.append(arrB[r])
        r += 1
    while l < len(arrA):
        merged_arr.append(arrA[l])
        l += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):    
    if len(arr) <= 1:  # base case
        return arr
        
    half = len(arr)//2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    print('Merged Arr: ', merge(left, right))
    return merge(left, right)

    # return arr

merge_sort([3, 5, 12, 1, 23, 22, 13, 4, 7, 2, 19, 6, 21, 14, 25, 34] )


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
