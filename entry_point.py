# A simple Python-esque swap routine
def swap(x, y):
    return y, x

if __name__ == '__main__':
    my_x = 5
    my_y = 3
    print(f'The reverse of ({my_x}, {my_y}), 3 is {swap(my_x, my_y)}')
