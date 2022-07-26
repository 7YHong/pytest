import numpy as np
list1=input('请输入4个数字\n').split()
list2=list(map(int,list1))
print('最大值：',max(list2))
print('最小值：',min(list2))
print('平均值：',np.mean(list2))