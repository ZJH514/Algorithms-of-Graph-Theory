import math
import re
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def is_all_zeros(Sequence):
    for i in Sequence:
        if i != 0:
            return False
    return True

def sort_max_index(Sequence, maxv):
    temp = Sequence[:]
    index = []  # 将度序列由大到小排列
    for i in range(maxv):  # 最大度
        index.append(temp.index(max(temp)))  # 将序列的最大值的index存入
        temp[index[i]] = 0  # 当前最大值复制为0，搜寻次大值
    return index

def Draw_Graph(Sequence, R=2):
    # 画出顶点, R决定画布的大小
    num = len(Sequence)
    alpha = []
    xarr = []
    yarr = []
    for i in range(0, num):
        alpha.append((2 * math.pi / num) * i)
        xarr.append(R * math.cos(alpha[i]))
        yarr.append(R * math.sin(alpha[i]))
        plt.text(xarr[i], yarr[i], f"v{i+1}\n{Sequence[i]}", fontsize=12, ha='center', va='center')
    plt.plot(xarr, yarr, 'ro')
    plt.axis('off')  # 不显示刻度

    Sequence.sort(reverse=True)  # 将序列排序，从大到小
    is_graph = True
    while not is_all_zeros(Sequence):
        maxv = max(Sequence)  # 最大度
        maxi = Sequence.index(maxv)  # 最大度顶点的下标
        Sequence[maxi] = 0  # TH4 delete d1 ===>  d1=0
        for i in sort_max_index(Sequence, maxv):  # d2---d(d1+1)的index
            if Sequence[i] > 0:
                plt.plot([xarr[maxi], xarr[i]], [yarr[maxi], yarr[i]], linewidth='1.0', color='green')  # 最大度点和其余>0度之间连线
                plt.pause(1)  # 暂停1秒
                Sequence[i] = Sequence[i] - 1  # d2---d(d1+1) 减一
            else:
                is_graph = False
                break
        if not is_graph:
            break
    return is_graph

def check_sequence():
    global CLEAR
    if CLEAR:
        CLEAR = False
        plt.cla()
        plt.axis('off')  # 不显示刻度
        canvas.draw()
        button.config(text='检查序列')
        label.config(text="请输入一个有限非负整数序列，用逗号分隔：")
    else:
        sequence = entry.get()  # 获取输入的序列
        sequence = sequence.strip()  # 去除前后的空格

        try:
            sequence = [int(x) for x in re.split(',|，', sequence)]  # 将输入的序列字符串转换为整数列表
            if min(sequence) < 0:
                label.config(text="有负数，请重新输入一个有限非负整数序列，用逗号分隔：")
                return
        except ValueError:
            label.config(text="无效的输入，请重新输入一个有限非负整数序列，用逗号分隔：")  # 输入不是有效的整数序列
            return

        if Draw_Graph(sequence, 2):
            plt.text(1.5, -2, 'YES', fontsize=20, color='blue')
            plt.show()
            CLEAR = True
            button.config(text='清除下方的图序列')
            label.config(text="该序列为图序列，下方给出示例图")
        else:
            plt.text(1.5, -2, 'NO', fontsize=20, color='red')
            plt.show()
            label.config(text="序列：{}不是图序列".format(entry.get().strip()))
            plt.cla()
            plt.axis('off')  # 不显示刻度
    return

CLEAR = False  # 全局变量

# 创建窗口
window = tk.Tk()
window.title("Havel-Hakimi")
window.geometry("1000x600")

# 创建标签和输入框
label = tk.Label(window, text="请输入一个有限非负整数序列，用逗号分隔：")
label.pack()  # 将部件放置到主窗口中

entry = tk.Entry(window)
entry.pack()  # 将部件放置到主窗口中

# 创建按钮
button = tk.Button(window, text="检查序列", command=check_sequence)
button.pack()  # 将部件放置到主窗口中

# 创建画布
f = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(f, master=window)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)

# 运行窗口,进入消息循环
window.mainloop()