import string
from random import choice
list1 = ['0','1']
random =  ''.join(choice(list1) for _ in range(4))
binary = int(random)

def binaryToDecimal(binary):
 
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)

if __name__ == '__main__':
    binaryToDecimal(binary)

