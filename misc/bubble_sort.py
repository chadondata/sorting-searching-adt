import random

def bubble_sort(my_list):
    n = len(my_list)

    swapped = False

    for i in range(n-1):
        for j in range(0, n-i-1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                swapped = True

        if not swapped:
            return
        
def main():
    my_list = []
    n = 100000

    for i in range(n):
        my_list.append(random.randint(0, n*10))

    print('Sorting')
    bubble_sort(my_list)
    print('Sorted')

main()
