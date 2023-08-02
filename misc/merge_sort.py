# merge sort
import random
from tqdm import tqdm

list_size = 1024 * 1024 * 256

big_list = []
for i in tqdm(range(list_size)):
    big_list.append(random.randint(0, list_size * 10))

my_list = [42, 76, 26, 18, 64]

def merge_sort(unsorted_list):
    if len(unsorted_list) == 1:
        return unsorted_list
    
    midpoint = len(unsorted_list) // 2
    left = merge_sort(unsorted_list[:midpoint])
    right = merge_sort(unsorted_list[midpoint:])

    sorted_list = []
    i = 0 # counter for the left
    j = 0 # counter for the right
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_list.append(right[j])
            j += 1
        else:
            sorted_list.append(left[i])
            i += 1
    
    if i < len(left):
        while i < len(left):
            sorted_list.append(left[i])
            i += 1

    if j < len(right):
        while j < len(right):
            sorted_list.append(right[j])
            j += 1

    return sorted_list

def main():
    print(my_list)
    new_list = merge_sort(my_list)
    print(new_list)

    new_big_list = merge_sort(big_list)
    print(new_big_list)

main()