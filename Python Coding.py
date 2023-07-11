
#10. write a program to find missing number in array?


def missing():
    sum1 = sum(a)
    n= a[-1]
    sum_natural = n*(n+1)//2

    missing = sum_natural -sum1
    print(missing)

a =[1,2,3,4,6,7,8,9]

missing()