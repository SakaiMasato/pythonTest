#线性均方差
def mseLinear(b, w, points):
    totalErr = 0
    for i in range(0, len(points)):
        x = points[i, 0] #获得i的x
        y = points[i, 1]  # 获得i的y

        #计算差的平方，累加误差
        totalErr += (y - (w * x + b)) ** 2
    #求平均，得到均方差
    return totalErr / float(len(points))