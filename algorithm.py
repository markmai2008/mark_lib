''' Mark 的算法模块
'''

from random import randint


def binary_search(nums, target):
    ''' 在升序排列的列表 nums 中二分查找 target 的位置
    返回第一个大于或等于 target 的位置下标
    '''
    n = len(nums)

    l = -1
    r = n
    while l < r - 1:
        m = (l + r) // 2
        if nums[m] < target:
            l = m
        else:
            r = m
    return r


def bubble_sort(nums):
    """ 冒泡排序法，将列表 num 进行排序，原位修改 nums 的内容
    """
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def my_min(nums):
    """ 输入一个列表，输出列表的最小值以及最小值所在的位置下标。
    如果列表中的元素有多个位置等于同一个最小值，输出较小的下标。
    :return: 返回两个元素的 tuple，第一个元素是 最小值所在的下标，
      第二个元素是最小值
    """
    n = len(nums)
    k = 0
    m = nums[0]
    for i in range(1, n):
        if nums[i] < m:
            m = nums[i]
            k = i
    return k, m


def selection_sort(nums):
    """ 选择排序法
    遍历 i，每次将 i 及后面的序列中的最小元素与 i 的位置互换
    """
    n = len(nums)
    for i, a in enumerate(nums):
        k = i
        m = nums[i]
        for j in range(i + 1, n):
            if nums[j] < m:
                m = nums[j]
                k = j
        nums[i], nums[k] = nums[k], nums[i]


if __name__ == '__main__':
    print('\n例五：随机生成测试')
    N = 20
    nums = [randint(0, 100) for i in range(0)]
    print(nums)
    print('期望的结果：', sorted(nums))
    selection_sort(nums)
    print('我的结果：', nums)
    # print(my_min(nums))
