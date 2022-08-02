while True:
    n=None
    try:
        n=int(input('请输入：'))
        if n<1:
            raise
    except KeyboardInterrupt:
        break
    except:
        print('输入的不是正整数！')
        continue
    
    sum=0
    sl=[]
    for i in range(n):
        sum+=i+1
        sl.append(i+1)
    
    print(' + '.join(map(str,sl)),'=',sum)