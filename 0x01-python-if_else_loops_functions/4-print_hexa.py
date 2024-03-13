#!/usr/bin/python3
def f_docTohex(n):
   return hex(n)

if __name__ == '__main__':
   for number in range(0, 99):
      print("{} = {}".format(number, f_docTohex(number)))
