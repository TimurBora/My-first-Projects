import random
def bubble_sort(list_x):
    index = 0
    for i in range((len(list_x) - 1) ** 2):
        if index > len(list_x) - 2:
            index = 0
        if list_x[index] > list_x[index + 1]:
            list_x[index], list_x[index + 1] = list_x[index + 1], list_x[index]
        index += 1
    return list_x


NUM = [random.randrange(-1, x) for x in range(500)]
print(bubble_sort(NUM[::-1]))

        
    
    
