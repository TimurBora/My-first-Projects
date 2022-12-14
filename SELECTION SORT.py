def selection_sort(array):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[j] < array[i]:
                array[j], array[i] = array[i], array[j]
    return array


NUM = [x for x in range(50)]
print(selection_sort(NUM[::-1]))
