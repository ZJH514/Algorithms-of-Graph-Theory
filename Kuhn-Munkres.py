import numpy as np
from scipy.optimize import linear_sum_assignment
import matplotlib.pyplot as plt

# 画出原图
def draw_graph(cost_matrix):
    n = len(cost_matrix)
    plt.figure()
    plt.imshow(cost_matrix, cmap='Blues')
    plt.colorbar()
    plt.title('Cost Matrix')
    plt.xlabel('Jobs')
    plt.ylabel('Workers')
    for i in range(n):
        for j in range(n):
            plt.text(j, i, str(cost_matrix[i][j]), ha='center', va='center', color='red')


# 解决最优匹配问题
def solve_matching(cost_matrix):
    # 使用Kuhn-Munkres算法计算最优匹配
    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    # 计算总成本
    total_cost = cost_matrix[row_ind, col_ind].sum()

    return row_ind, col_ind, total_cost

# 权值矩阵
cost_matrix = np.array([[10, 5, 9, 20],
                        [8, 15, 7, 11],
                        [11, 7, 14, 6],
                        [12, 10, 13, 6]])
draw_graph(cost_matrix)

row_ind, col_ind, total_cost = solve_matching(cost_matrix)
print("最优匹配结果：")
for i in range(len(row_ind)):
    print("  Worker {} is assigned to Job {}".format(row_ind[i]+1, col_ind[i]+1))
print("最优总成本：", total_cost)
plt.show()