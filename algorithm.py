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


def insertion_sort(nums):
    """插入排序法
    遍历 left的长度i，从后往前遍历left中的元素nums【k】，如果nums【k】大于nums【k+1】，将它们交换，否则结束循环，进入下一个i
    """
    n = len(nums)
    for i in range(1, n):
        for k in range(i-1, -1, -1):
            if nums[k] > nums[k+1]:
                nums[k], nums[k+1] = nums[k+1], nums[k]
            else:
                break


def merge_sort(nums, l=0, r=-1):
    """归并排序法
    锚例当前排序的部分只有一个元素的时候，直接返回。
    将列表分成左右两边。
    递归调用排序方法，对左边部分进行排序。
    递归调用排序方法，对右边部分进行排序。
    将左边和右边拷贝一份，然后合并到原来的位置。
    """
    n = len(nums)
    if r == -1:
        r = n
    if r - l == 1:
        return
    m = (l + r) // 2
    merge_sort(nums, l, m)
    merge_sort(nums, m, r)
    a1 = nums[l:m]
    a2 = nums[m:r]
    k = l
    i = 0
    j = 0
    while k < r:
        if i >= len(a1):
            nums[k] = a2[j]
            j += 1
        elif j >= len(a2):
            nums[k] = a1[i]
            i += 1
        elif a1[i] < a2[j]:
            nums[k] = a1[i]
            i += 1
        else:
            nums[k] = a2[j]
            j += 1
        k += 1


def merge_sort1(nums, l=0, r=-1):
    n = len(nums)
    if r == -1:
        r = n
    if r - l == 1:
        return
    m = (l + r) // 2
    merge_sort1(nums, l, m)
    merge_sort1(nums, m, r)
    a1 = nums[l:m]
    a2 = nums[m:r]
    k = l
    i = 0
    j = 0
    while k < r:
        if i >= len(a1):
            nums[k] = a2[j]
            j += 1
        elif j >= len(a2):
            nums[k] = a1[i]
            i += 1
        elif a1[i] < a2[j]:
            nums[k] = a1[i]
            i += 1
        else:
            nums[k] = a2[j]
            j += 1
        k += 1


if __name__ == '__main__':
    print('\n例五：随机生成测试')
    N = 20
    nums = [randint(0, 100) for i in range(10)]
    print(nums)
    print('期望的结果：', sorted(nums))
    from time import time

    # print('插入排序法：', end='')
    # t0 = time()
    # insertion_sort(nums[:])
    # print('耗时：', time()-t0)

    # print('冒泡排序法：', end='')
    # t0 = time()
    # bubble_sort(nums[:])
    # print('耗时：', time()-t0)

    # print('选择排序法：', end='')
    # t0 = time()
    # selection_sort(nums[:])
    # print('耗时：', time()-t0)

    # print('归并排序法：', end='')
    # t0 = time()
    # merge_sort(nums[:])
    # print('耗时：', time()-t0)

    merge_sort1(nums)
    print('我的结果  ：', nums)
    # print(my_min(nums))
