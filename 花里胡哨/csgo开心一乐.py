import random
import time

while True:
    m = 0
    t = 0
    y = 0
    lan = 0
    zi = 0
    fen = 0
    hong = 0
    jin = 0
    for n in range(0, 20):
        print("-", end='')
    print("抽奖游戏开始", end='')
    for n in range(0, 20):
        print("-", end='')
    print()
    c = int(input("请选择抽奖次数:"))
    for n in range(1, c + 1):
        t = t + 17
        # time.sleep(1)
        x = random.randint(1, 10000)
        print("x=%d" % x)
        if x <= 7991:
            y = random.randint(1, 6)
            lan = lan + 1
            m = m + y
            print("开出了军规级皮肤(蓝色)")
        elif 7991 < x <= 9589:
            y = random.randint(5, 20)
            zi = zi + 1
            m = m + y
            print("一般般,开出了受限级皮肤(紫色)")
        elif 9589 < x <= 9909:
            y = random.randint(20, 100)
            fen = fen + 1
            m = m + y
            print("还可以,开出了保密级皮肤(粉色)")
        elif 9909 < x <= 9974:
            y = random.randint(70, 500)
            hong = hong + 1
            m = m + y
            print("不错,开出了隐秘级皮肤(红色)")
        elif 9974 < x <= 10000:
            y = random.randint(500, 5000)
            jin = jin + 1
            m = m + y
            print("运气爆棚开出了金色传说")
        print("价值%drmb" % y)
    for n in range(0, 20):
        print("-", end='')
    print("抽奖游戏结束", end='')
    for n in range(0, 20):
        print("-", end='')
    print()
    print("本次抽奖花费%drmb,获得%drmb" % (t, m))
    print("蓝%d个,紫%d个,粉%d个,红%d个,金%d个" % (lan, zi, fen, hong, jin))
    a = int(input("输入0退出,其他数继续!:"))
    if a == 0:
        break
