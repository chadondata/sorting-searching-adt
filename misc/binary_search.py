
def binary_search(data, the_list):
    if len(the_list) < 1:
        return False
    
    lower = 0
    midpoint = len(the_list) // 2
    upper = len(the_list) - 1

    while lower <= upper:
        midpoint = (upper + lower) //2
        if data > the_list[midpoint]:
            lower = midpoint + 1
        elif data < the_list[midpoint]:
            upper = midpoint - 1
        else:
            return True
        
    return False

def main():
    my_list = []

    for i in range(1024 * 1024 * 128):
        my_list.append(i * 2)
    print(f'Testing sort on list of size {len(my_list)}')
    print(f'Looking for 30: {binary_search(30, my_list)}')
    print(f'Looking for -1: {binary_search(-1, my_list)}')
    print(f'Looking for 101: {binary_search(101, my_list)}')
    print(f'Looking for 10001: {binary_search(10001, my_list)}')
    print(f'Looking for 0: {binary_search(0, my_list)}')
    print(f'Looking for 1998: {binary_search(1998, my_list)}')

main()
