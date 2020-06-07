"""
向一个空栈中一次输入正整数，假设入栈元素N（1<=N<=2^31-1）,按顺序以此为Nx...N4、N3、N2、N1，每当元素入栈时，
如果N1=N2+，，，+Ny（y的范围[2,x],1<=x<=1000）,则N1~Ny全部元素出栈，重新入栈新元素M（M=2*N1）。
如以此向栈中存入6，1，2，3，当存入6，1，2时，栈底至栈顶依次为[6,1,2],当存入3时，3=2+1，3，2，1全部出栈，
重新入栈元素6（6=2*3），此时栈中有元素6，因为6=6，所以两个6全部出栈，存入12，最终栈中只剩下一个元素12。
输入描述：
使用单个空格隔开的正整数字符串。
如”5 6 7 8“，左边的数字先入栈，输入的正整数个数为x，1<=x<=1000。
输出描述：最终栈中存留的元素值，元素值使用空格隔开，如”8 7 6 5“，栈顶数字在最左边。
示例1：
输入：5 10 20 50 85 1
输出：1 170
输入：3 5 10 20 50 85 1
输出：1 170 3
输入：6 1 2 3
输出：12
输入：20 6 1 2 3 2
输出：2 12 20
"""
class ss():
    def __init__(self):
        print(self.out_put("20 6 1 2 3 2"))

    def out_put(self, input_str):
        str_list = list(map(int, input_str.strip().split(" ")))
        # 输入一个数，直接输出
        if len(str_list) == 1:
            return " ".join(list(map(str, str_list)))
        current_list = []
        current_list.append(str_list[0])
        for i in range(1, len(str_list)):
            current_list = self.select(current_list, str_list[i])
        # 翻转
        current_list.reverse()
        return " ".join(list(map(str, current_list)))

    def select(self, current_list, s_str):
        sum = 0
        # 从栈顶取值
        for j in current_list[-1::-1]:
                sum += j
                if sum == s_str:
                    # 出栈
                    current_list = current_list[:current_list.index(j)]
                    s_str = 2 * s_str
                    # 栈中还有值，继续判断
                    if len(current_list) > 0:
                        # 每进行一次递归，栈改变一次
                        current_list = self.select(current_list, s_str)
                    # 栈中没有值，直接入栈
                    else:
                        current_list.append(s_str)
                    return current_list
        # N1 ！= N2+，，，+Ny
        current_list.append(s_str)
        return current_list

ss()