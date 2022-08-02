def paint(x):
    print('\n输出直角三角形:')
    i = 0
    while i < x:
        i += 1
        print('*'*i)

    print('\n输出等腰三角形:')
    for i in range(x):
        print(' '*(x-i-1), end='')
        print('*'*(2*i+1))

    print('\n输出梯形:')
    for i in range(x):
        print(' '*(x-i-1), end='')
        print('*'*(2*i+3))


x = None
try:
    x = int(input('请输入图形行数：'))
except KeyboardInterrupt:
    None
except:
    print('请输入正整数！')
else:
    paint(x)
