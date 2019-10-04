# Дано натуральне число n.
# a) з'ясувати, чи входить цифра 3 в запис числа n^2
# b) змінити порядок цифр числа n на зворотній

def is_3_in_nn(number):
    '''з'ясувати, чи входить цифра 3 в запис числа n^2'''
    for i in range(len(str(number**2))):
        if str(number**2)[i]=='3':
            return True
    return False


def reverse_number(number):
    '''змінити порядок цифр числа n на зворотній'''
    reversed_num=0
    while number>0:
        reversed_num=reversed_num*10+number%10
        number=number//10
    return reversed_num
