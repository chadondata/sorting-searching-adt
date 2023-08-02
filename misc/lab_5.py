# A binary representation of an integer
#  is a series of 1s and 0s
# Starting at the farthest right:
# a 1 on the last position is worth 2^0 (aka 1)
# Each position to thr left increases the exponent by 1
# There are 10 kinds of people in the world. Those who
#   know binary and those who don't.
bits = 16
def int_to_bin(n, b):
    if b == 1:
        if n == 0:
            return '0'
        else:
            return '1'
    if n >= (2**(b-1)):
        remainder = n - (2**(b-1))
        return f'1{int_to_bin(remainder, b-1)}'
    else:
        return f'0{int_to_bin(n, b-1)}'
    
value = int(input("Enter an unsigned integer: "))
print(int_to_bin(value, bits))
