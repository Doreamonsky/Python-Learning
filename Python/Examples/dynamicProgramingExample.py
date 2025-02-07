# 爬楼梯
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。

# 示例 1：

# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# https://leetcode-cn.com/explore/interview/card/top-interview-questions-easy/23/dynamic-programming/54/


def climbLadder(n):
    # 边界
    a = 1
    b = 2

    fn = 0

    if (n <= 2):
        return n

    for i in range(3, n + 1):  # range 函数前闭后开
        # 状态转移函数
        fn = a + b
        a = b
        b = fn

    return fn


print(climbLadder(13))


# https://www.jianshu.com/p/ef1abd49c007
# 算法：动态规划解决<国王和金矿>
#
