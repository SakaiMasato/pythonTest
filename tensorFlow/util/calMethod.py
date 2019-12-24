from tensorFlow.util.ErrorUtil import mseLinear as mse
#梯度下降计算梯度
def step_gradient(b_current, w_current, points, lr):
    #计算误差函数在所有点上的导数
    b_gradient = 0
    w_gradient = 0

    #样本总数
    M = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0] #获得i的x
        y = points[i, 1]  # 获得i的y

        #误差函数对b的导数： grab_b = 2/M(wx + b -y)
        b_gradient += 2/M * (w_current * x + b_current - y)

        # 误差函数对w的导数： grab_b = 2/M(wx + b -y)
        w_gradient += 2/M * (w_current * x + b_current - y) * x

        new_b = b_current - lr * b_gradient #lr为学习率
        new_w = w_current - lr * w_gradient
    return [new_b, new_w]

#梯度更新
def gradient_descent(points, starting_b, starting_w, lr, num_iterations):
    # 更新w,b
    b = starting_b
    w = starting_w
    for step in range (num_iterations):
        b, w = step_gradient(b, w, points, lr)
        loss = mse(b, w, points)
        if step % 50 == 0: #打印误差和实时w,b
            print(f"iteration:{step}, loss:{loss}, w:{w}, b:{b}")
    return [b, w]