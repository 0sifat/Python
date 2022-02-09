import re


def valu_return(value_1,value_2):

    sum = value_1 + value_2
    sub = value_2 - value_1

    return sum, sub





calculation =valu_return(23,44)
print (calculation)

#Solution 2

def valu_return(value_3,value_4):

 return value_3 + value_4 , value_4 - value_3

bal, cal = valu_return(23,54)
print(bal,cal)