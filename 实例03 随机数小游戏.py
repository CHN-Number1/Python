# _*_ coding:utf-8 _*_
# CHN-Number1
# 本实例:随机数小游戏
# 生成随机数,用户输入一个数字猜.
# 如果数字比随机数大,提示数字大了,反之提示小了.
# 导入随机数random模块
import  random
# i 为用户猜的次数
i = 1
# a 为随机数0-100
a = random.randint(0,100)
# b 为用户输入的数字
print('本次小游戏为猜数字,随机数为0-100')
b = int(input('请输入一个整数:'))
while a != b:
    if b > a:
        print('你输入的数字大了')
        b = int(input('请再次输入:'))
    else:
        print('你输入的数字小了')
        b = int(input('请再次输入:'))
    i += 1
else:
    # format函数为对 i 格式化
    print('恭喜你在第{0}次终于猜对啦!'.format(i))
