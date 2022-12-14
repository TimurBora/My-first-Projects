def insertion_sort(arr):
    s = -1
    for i in range((len(arr) - 1)  ** 2):
        s += 1
        if s > len(arr) - 1:
            s = 0
        current = arr[s]
        j = s - 1
        while j >=0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr


ARR = [x for x in range(5000)]
print(insertion_sort(ARR[::-1]))
    
