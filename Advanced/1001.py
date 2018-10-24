#coding:utf-8

#次方的表示方法
lower_margin = -10 ** 6
upper_margin = 10 ** 6

if __name__ == '__main__':
    #split()是用来识别空格
    #直接input()输入的是class类型
    a, b = input().split()
    A = int(a)
    B = int(b)
    if type(A) is not int:
        print('the type of "a" is wrong')
    elif type(B) is not int:
        print('the type of "b" is wrong')
    elif A < lower_margin or A > upper_margin:
        print('"a" is out of range')
    elif B < lower_margin or A > upper_margin:
        print('"b" is out of range')
    else:
        c = A + B
    #format()的用法，‘:’后接的是format处理的方式
    print("{:,}".format(c))
