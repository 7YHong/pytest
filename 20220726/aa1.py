i=5
while i>0:
    i-=1
    print('*',end='')
    if i==4 or i==0:
        symbal='*'
    else:
        symbal=' '
    j=48
    while j>0:
        j-=1
        print(symbal,end='')
    print('*')

