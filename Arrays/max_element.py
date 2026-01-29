def find_max(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element

arr = [3, 7, 2, 9, 5]
print("Maximum element is:", find_max(arr))
#Maximum element is: 9
