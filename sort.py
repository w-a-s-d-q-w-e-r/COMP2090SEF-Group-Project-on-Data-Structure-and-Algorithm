def insertion_sort(arr, left=0, right=None):
    # Base case: if the array is already sorted, do nothing
    if right is None:
        right = len(arr) - 1

    # Iterate through the array, starting from the second element
    for i in range(left + 1, right + 1):
        # Select the current element
        key_item = arr[i]

        # Compare the current element with the previous one
        j = i - 1

        # While the previous element is greater than the current one,
        # shift the previous element to the next position
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1

        # Once the loop ends, the previous element is less than or equal to
        # the current element, so place the current element after it
        arr[j + 1] = key_item

    return arr


def merge(left, right):
    # If the left subarray is empty, return the right subarray
    if not left:
        return right

    # If the right subarray is empty, return the left subarray
    if not right:
        return left

    # Compare the first elements of the two subarrays
    if left[0] < right[0]:
        # If the first element of the left subarray is smaller,
        # recursively merge the left subarray with the right one
        return [left[0]] + merge(left[1:], right)
    else:
        # If the first element of the right subarray is smaller,
        # recursively merge the right subarray with the left one
        return [right[0]] + merge(left, right[1:])


def tim_sort(arr):
    # Initialize the minimum run size
    min_run = 32

    # Find the length of the array
    n = len(arr)

    # Traverse the array and do insertion sort on each segment of size min_run
    for i in range(0, n, min_run):
        insertion_sort(arr, i, min(i + min_run - 1, (n - 1)))

    # Start merging from size 32 (or min_run)
    size = min_run
    while size < n:
        # Divide the array into merge_size
        for start in range(0, n, size * 2):
            # Find the midpoint and endpoint of the left and right subarrays
            midpoint = start + size
            end = min((start + size * 2 - 1), (n - 1))

            # Merge the two subarrays
            merged_array = merge(arr[start:midpoint], arr[midpoint:end + 1])

            # Assign the merged array to the original array
            arr[start:start + len(merged_array)] = merged_array

        # Increase the merge size for the next iteration
        size *= 2

    return arr
  
  
 # Using the sorted() function
a = [5, 3, 1, 4, 6, 2]
sorted_list = tim_sort(a)
print("Sorted list using Tim Sort:", sorted_list)
