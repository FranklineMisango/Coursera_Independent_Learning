def merge(arr, left, right):
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def mergeSort(arr):
    if len(arr) < 2:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    mergeSort(left)
    mergeSort(right)
    merge(arr, left, right)

arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)

mergeSort(arr)

print("Sorted array:", arr)
