# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime

def run_time(func):
    def inner():
        start = datetime.datetime.now()
        func()
        end = datetime.datetime.now()
        return  end-start
    return inner

@run_time
def func1():
    num = 5000000
    while (num > 0):
        num = num - 1

@run_time
def func2():
    num = 5000
    while(num>0):
        num = num-1
        num2 = 5000
        while(num2>0):
            num2 = num2-1
dict = {}
def cache(func):
    def inner(n):
        if dict.keys().__contains__(n):
            return dict[n]
        else:
            num = func(n)
            dict[n] = num
            return  dict[n]
    return inner
@cache
def fibu(n):
    num1 = 1
    num2 = 1
    num3 = num1+num2
    if n==0:
        return 0
    if n==1:
        return num1
    if n==2:
        return num2
    while(n>0):
        num1 = num2
        num2 = num3
        num3 = num1+num2
        dict[n] = num3
        n = n-1
    return num3



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(func1())
    # print(func2())
    print(fibu(5))
    fibu(5)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
