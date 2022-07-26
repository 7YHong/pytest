dict1={
    1:'星期一',
    2:'星期二',
    3:'星期三',
    4:'星期四',
    5:'星期五',
    6:'星期六',
    7:'星期日',
}

list1=list(map(int,input('请输入数组：\n').split()))
if max(list1)>7 or min(list1)<1:
    print('超出范围')
else:
    for i in list1:
        print(dict1[i])