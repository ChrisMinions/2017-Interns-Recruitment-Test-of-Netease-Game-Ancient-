'''
[编程题] 赛马
时间限制：1秒
空间限制：32768K
在一条无限长的跑道上，有N匹马在不同的位置上出发开始赛马。
当开始赛马比赛后，所有的马开始以自己的速度一直匀速前进。
每匹马的速度都不一样，且全部是同样的均匀随机分布。
在比赛中当某匹马追上了前面的某匹马时，被追上的马就出局。 
请问按以上的规则比赛无限长的时间后，赛道上剩余的马匹数量的数学期望是多少 
输入描述:
每个测试输入包含1个测试用例
输入只有一行，一个正整数N
1 <= N <= 1000


输出描述:
输出一个浮点数，精确到小数点后四位数字，表示剩余马匹数量的数学期望

输入例子1:
1
2

输出例子1:
1.0000
1.5000
'''

'''
解题思路：递归
  用expert函数求取剩余马匹数量的期望值，很明显，当马匹数量为1时，期望值是1
  当马匹数量为n时，位于最前面的马速度最快的概率是1/n，因此他被剩下的期望是1*1/n，（如果不是最快则必定会被淘汰）
  那么剩下的n-1匹马中，位于最前面的马速度最快的概率是1/(n-1)，因此他被剩下的期望是1*1/(n-1)
  前两匹马剩下的概率就是 1/n + 1/(n-1)
  如此递归，直至只剩下一匹马，则返回1
  由于python有一个默认递归深度限制，所以要想实现100%AC，得先把默认的递归深度改了
'''

'''
代码运行结果：
答案正确:恭喜！您提交的程序通过了所有的测试用例
'''

import sys
sys.setrecursionlimit(1000000)

N = int(input())


def expert(n):
    if n == 1:
        return 1
    else:
        return 1/n+expert(n-1)

print('%.4f' % expert(N))
