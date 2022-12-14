def sort(arr):
    i = 0
    while i < len(arr) - 1:
        m = i
        j = i + 1
        while j < len(arr):
            if arr[j] < arr[m]:
                m = j
            j += 1
        arr[i], arr[m] = arr[m], arr[i]
        i += 1
    return arr
                

ARR = [77, 46, 11, 89, 48, 14, 67, 73, 22, 26]
print(sort(ARR))
        
            
