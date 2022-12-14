def quick_sort(list_x):
    if len(list_x) < 2:
        return list_x
    else:
        pivot = list_x[0]
        less = [x for x in list_x[1:] if x <= pivot]
        greater = [x for x in list_x[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

NUM = [x for x in range(2000)]
print(quick_sort(NUM[::-1]))
