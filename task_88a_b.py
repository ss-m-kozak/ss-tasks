# Дано натуральне число n.
# a) з'ясувати, чи входить цифра 3 в запис числа n^2
# b) змінити порядок цифр числа n на зворотній

def is_3_in_nn():
    '''з'ясувати, чи входить цифра 3 в запис числа n^2'''
    try:
        number=int(input("Enter number:"))
        for i in range(len(str(number**2))):
            if str(number**2)[i]=='3':
                return True
        return False
    except ValueError:
        return "Please enter the number"


def reverse_number():
    '''змінити порядок цифр числа n на зворотній'''
    try:
        number=int(input("Enter number:"))
        reversed_num=0
        while number>0:
            reversed_num=reversed_num*10+number%10
            number=number//10
        return reversed_num
    except ValueError:
        return "Please enter the number"

# print(is_3_in_nn())
# print(reverse_number())
