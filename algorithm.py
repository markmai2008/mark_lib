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
    while l < r -1:
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
        




if __name__ == '__main__':
    print('\n例五：随机生成测试')
    N = 20
    nums = [randint(0, 1000) for i in range(20)]
    print('期望的结果：', sorted(nums))
    bubble_sort(nums)
    print('我的结果：', nums)

    
