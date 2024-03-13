#!/usr/bin/python3
def f_docTohex(n):
   return hex(n)

if __name__ == '__main__':
   for number in range(0, 99):
    if number < 98:
        print(number, end=", ")
    else:
        print(number, end="")
