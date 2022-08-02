input1=input('请输入字符串：')
li=list(input1)
print('列表：',li)
li.sort()
print('排序后的列表：',li)
ls=set(li)
print('集合',ls)
ld={}
for key in ls:
    ld[key]=li.count(key)
print('计数字典：',ld)