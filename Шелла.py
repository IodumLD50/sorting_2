# Shell sort
# Сортировка Шелла


import random

n = 100
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)
print('Not sorted:')
print(arr)
print('-------------')

#######################################################  
 
#                       |МОДИФИКАЦИЯ|

step = len(arr) // 2 # оприеделяем шаг (step), длину нашего списка (len(arr)) // 2
while step > 0:
    for i in range(step, n, 1):
#       value = arr[i] # сохраняем значение
        current_index = i # текущий индекс
        index_to_check = current_index - step # индекс с которым будем сравнивать
        while (current_index > 0 and
               # < от большего к меньшему > от меньшего к большему (arr[index_to_check] > arr[current_index])
               arr[index_to_check] > arr[current_index]): #вместо "vaiue" arr[current_index]
#           arr[current_index] = arr[index_to_check] 
            #_______________swap_________________________
            # логика по замене
            temp = arr[current_index]  
            arr[current_index] = arr[index_to_check]
            arr[index_to_check] = temp
            #_______________swap_________________________
            current_index -= step
            index_to_check -= step
#       arr[current_index] = value    
    step = step // 2




# step = len(arr) // 2 # оприеделяем шаг (step), длину нашего списка (len(arr)) // 2
# while step > 0:
#     for i in range(step, n, 1):
#         value = arr[i] # сохраняем значение
#         current_index = i # текущий индекс
#         index_to_check = current_index - step # индекс с которым будем сравнивать
#         while (current_index > 0 and arr[index_to_check] > value):
#             arr[current_index] = arr[index_to_check]
#             current_index -= step
#             index_to_check -= step
#         arr[current_index] = value    
#     step = step // 2
#######################################################   

print('Sorted:')
print(arr)