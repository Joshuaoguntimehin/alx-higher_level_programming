#!/usr/bin/python3
if __name__ == '__main__':
    for i in range(0, 10):
        for j in range(0, 10):
            if i == 9 and j == 9:
                print("{}{}".format(i, j), end="")
            else:
                print("{}{}".format(i, j), end=", ")
