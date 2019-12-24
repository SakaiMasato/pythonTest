import numpy as np
from tensorFlow.util.ErrorUtil import mseLinear as mse
from tensorFlow.util.calMethod import gradient_descent as gd

data = []   #保存样本

#学习率
lr = 0.01
initial_b = 0
initial_w = 0
#训练次数
num_iterations = 1000

for i in range(100):    #循环采样
    x = np.random.uniform(-10., 10.)    #取值(-10,10)

    #高斯噪声
    eps = np.random.normal(0., 0.01)    #正态分布(0,0.01)

    #模型输出
    y = 1.477 * x + 0.089 + eps

    data.append([x, y]) #保存样本
data = np.array(data)
[b,w] = gd(data, initial_b, initial_w, lr, num_iterations)
loss = mse(b, w, data) # 计算最优数值解w,b 上的均方差
print(f'Final loss:{loss}, w:{w}, b:{b}')



