"""
File name: Inversion counting - divide and conquer
Author: Stuti Pandey

"""

def merge_and_count(arr, temp_arr, left, right):
    # A helper function to merge two halves of the array and count inversions.

    if left == right:
        return 0
    
    mid = (left + right) // 2
    inv_count = 0
    
    inv_count += merge_and_count(arr, temp_arr, left, mid)  # Count inversions in left half
    inv_count += merge_and_count(arr, temp_arr, mid + 1, right)  # Count inversions in right half
    inv_count += merge(arr, temp_arr, left, mid, right)  # Count inversions while merging
    
    return inv_count

def merge(arr, temp_arr, left, mid, right):
    # A function to merge two sorted halves of an array and count inversions.

    i = left    # Starting index for left subarray
    j = mid + 1  # Starting index for right subarray
    k = left    # Starting index to be sorted
    inv_count = 0
    
    # Merge the two halves into the temp array
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid-i + 1)  
            j += 1
        k += 1
    
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]
    
    return inv_count

def count_inversions(arr):
    """
    Function to count inversions in an array using merge sort.
    """
    temp_arr = [0] * len(arr)
    return merge_and_count(arr, temp_arr, 0, len(arr) - 1)

def main():
    outputs = []
    k = int(input())  
    for _ in range(k):
        j = int(input()) 
        arr = list(map(int, input().split()))  
        outputs.append(count_inversions(arr))

    for output in outputs:
        print(output)  

if __name__ == "__main__":
    main()
