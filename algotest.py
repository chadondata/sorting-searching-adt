from algorithms import Sorting

import random

lst = []
n = 50
for i in range(n):
    lst.append(random.randint(0, n*2))

print(lst)
lst = Sorting.default_sort(lst)
print(lst)
