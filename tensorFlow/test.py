import tensorflow as tf
import numpy as np

#标量张量
a = 1.2
aa = tf.constant(1.2) #tensorflow 形式的标量张量
print(type(a), tf.is_tensor(a), type(aa), tf.is_tensor(aa))

#向量张量
x = tf.constant([1, 2., 3.3])
print(x.numpy())
print(type(x), tf.is_tensor(x))

#矩阵张量
a = tf.constant([[1,2],[3,4]])
print(a)

#3维张量
a = tf.constant([[[1,2],[3,4]],[[5,6],[7,8]]])
print(a)

#字符
a = tf.constant('hello, deep learning')
print(a)
a = tf.constant('hello, deep learning')
print(tf.strings.upper(a))

#布尔(tf的布尔类型与python的不相等)
a = tf.constant(True)
print(a)

#创建张量的时候可以指定精度tf.float64即tf.double
a = tf.constant(1234567, dtype = tf.int16)
print(a)
if a.dtype == tf.int16:
    a = tf.cast(a,tf.int32)
    print(a.dtype)

#创建需要被优化的张量
a = tf.Variable([1,2],[3,4])
print(a)

#从 Numpy, List 对象创建张量
a = tf.convert_to_tensor([1, 2])
print(a)
a = tf.convert_to_tensor(np.array([[1, 2],[3, 4]]))
print(a)

#全0标量张量, 全1标量张量
print(tf.zeros([]))
print(tf.ones([]))

#全0向量张量, 全1向量张量
print(tf.zeros([1]))
print(tf.ones([1]))

#全0向量矩阵, 全1向量矩阵
print(tf.zeros([2,2]))
a = tf.ones([4,2])
print(tf.ones([4,2]))

#采用某种格式建立新的向量张量
print(tf.zeros_like(a))
a = tf.zeros([2,2])
print(tf.ones_like(a))

#创建自定义数值张量
print(tf.fill([], -1))

#所有元素为-1的向量张量
print(tf.fill([1], -1))

#所有元素为-1的矩阵
print(tf.fill([2,2], -1))

#创建均值为0标准差为1的正态分布
print(tf.random.normal([2,2]))
#创建均值为1标准差为2的正态分布
print(tf.random.normal([2,2], mean = 1, stddev = 2))

#采样自区间[0,1],shapr为[2,2]均匀分布
print(tf.random.uniform([2,2]))
print(tf.random.uniform([2,2], maxval=10))
print(tf.random.uniform([2,2],maxval=100,dtype=tf.int32))

#创建整形序列
print(tf.range(10))
print(tf.range(10, delta=2))
print(tf.range(2, 10, delta=2))



