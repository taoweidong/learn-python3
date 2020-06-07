"""
屏幕给出1~9中任意3个不重复的数字，大家以最快的时间给出这几个数字可以拼成的数字从小到大排列位于第N位置的数字，
其中N为给出数字中最大的（如果不到这么多数字，则给出最后一个即可）。
注意：
1、2可以当作5来使用，5可以当作2来使用进行数字拼接，且屏幕不能同时给出2和5；
2、6可以当作9来使用，9可以当作6来使用进行数字拼接，且屏幕不能同时给出6和9；
如果给出1，4，8，则可以拼接成的数字为1，4，8，14，18，41，48，81，84，148，184，418，481，814，841。
那么最第N（即8)个数字为81。
输入描述：输入以逗号分隔的描述3个int类型整数的字符串。
输出描述：
输出为这几个数字可以拼成的数字，从小到大排列于第N（N为输入数字中最大的数字）位置的数字，
如果输入的数字不在范围内或者有重复，则输出-1。
示例：
输入
1,4,8
输出
81
"""
import itertools


class ss():
    def __init__(self):
        self.select_n("1,2,6")

    def select_n(self, ss_str):
        input_str = "".join(ss_str.strip().split(","))
        # 输入错误判断：1.为空或者不等于3； 2.有重复； 3.有负数（根据题目要求判断）
        if not input_str or len(input_str) != 3:
            print(-1)
        set_str = "".join(list(set(input_str)))
        if "2" in input_str and "5" in input_str or "6" in input_str and "9" in input_str \
                or len(input_str) != len(set_str):
            print(-1)
        # if min(input_str) < 0:
        #     print(-1)

        # 找最大数
        N = max(list(map(int, set_str)))
        out_put = []

        # 输入赋值
        for i in range(1, len(set_str) + 1):
            self.permutations(set_str, out_put, i)

        # 2/5,6/9替换排列
        if "2" in set_str:
            replace_str = set_str.replace("2", "5")
            for i in range(1, len(replace_str) + 1):
                self.permutations(replace_str, out_put, i)
        elif "5" in set_str:
            replace_str = set_str.replace("2", "5")
            for i in range(1, len(replace_str) + 1):
                self.permutations(replace_str, out_put, i)
        elif "6" in set_str:
            replace_str = set_str.replace("6", "9")
            for i in range(1, len(replace_str) + 1):
                self.permutations(replace_str, out_put, i)
        elif "9" in set_str:
            replace_str = set_str.replace("9", "6")
            for i in range(1, len(replace_str) + 1):
                self.permutations(replace_str, out_put, i)

        # 对输出去重，排序
        out_put = list(map(int, out_put))
        out_put = sorted(list(set(out_put)))

        # 输出
        print(out_put)
        print(out_put[N - 1])

    def permutations(self, input_str, out_put, count):
        for i in itertools.permutations(input_str, count):
            out_put.append("".join(i))


ss()
