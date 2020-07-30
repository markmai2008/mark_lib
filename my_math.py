def fact(n):
    """ 计算一个整数的阶乘
    输入一个正整数 n, 返回 n*(n-1)*(n-2)*...*1 的值
    """
    a = 1
    for i in range(n):
        a = a*(n-i)
    return a


def fact_recursive(n):
    """用递归计算一个整数的阶乘
    """
    if n < 1:
        return -1
    if n == 1:
        return 1
    return n * fact_recursive(n - 1)


def gcd(m, n):
    """计算两个整数的最大公因数
    输入两个正整数 m和 n，返回 m和 n的最大公因数
    """
    a = 1
    for i in range(min(m, n)):
        if m % (i + 1) == 0 and n % (i + 1) == 0:
            a = i+1
    return a


def gcd2(m, n):
    """ 使用辗转相除法递归计算最大公约数 """
    if n == 0:
        return m
    return gcd2(n, m % n)


def sqr(m):
    """计算一个整数平方根
    输入一个正整数 m，返回 m的整数平方根，如果不存在，返回-1
    """
    a = 1
    while True:
        if a * a == m:
            return a
        elif a * a > m:
            return -1
        a = a + 1
# while a * a <= m:
##        print('a = ', a)
# if a * a == m:
# return a
##        a += 1
# return -1


def factor_list(m):
    """找出正整数 m的所有质因数
    输入一个正整数 m，返回一个列表，列表内包含了 m的所有质因数  列如：输入12，输出【2,2,3】
    """
    a = []
    b = 2
    while True:
        # print(b)
        if m % b == 0:
            a.append(b)
            m //= b
            continue
        elif b > m:
            break
        b += 1
    return a


if __name__ == '__main__':
    # print('这是 function 模块的主程序测试内容')
    # print('100 的质因数是 ', factor_list(100))
    # print(fact_recursive(0))
    print(gcd2(-3, -12))
