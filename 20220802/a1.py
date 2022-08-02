sm = {
    85: 'S',
    80: 'A',
    60: 'B',
    0: 'C'
}
score = None
try:
    score = float(input('请输入分数'))
    if score > 100 or score < 0:
        raise
except:
    print('请输入0-100的一个整数或小数！')
else:
    for key in sm:
        if score >= key:
            print(sm[key]+'档')
            break
