#Реализуйте алгоритм перемешивания списка.

import random
list = [1,2,3,4,5]
for i in range(len(list)):
    index_a=random.randint(0, len(list)-1)
    temp=list[i]
    list[i] = list[index_a]
    list[index_a]=temp
print(list)

# from random import shuffle
# list = [1,2,3,4,5]
# shuffle(list)
# print(list)

