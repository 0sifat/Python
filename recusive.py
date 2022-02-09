import re


def recursice_function (num):

    if num :
        return num + recursice_function(num - 1)
        

    else:
        return 0 
        print("Heloo")





test=recursice_function(2)

print(test)