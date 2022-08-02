import random
list1 = [4, 5, 6]
dict1 = {
    0: '平局，再来一次吧!',
    1: '你赢了!',
    2: '你输了!'
}
while True:
    try:
        n = int(input('请输入：石头(1)、剪刀(2)、布(3)：'))
        if n < 1 or n > 3:
            print('输入错误，请重新输入！')
            continue
    except KeyboardInterrupt:
        break
    except:
        continue
    res = random.choice(list1)
    print('电脑出', res-3, dict1[(res-n) % 3])
