import tensorflow as tf

# calculate the slope of 'y = ax^2 + bx + c'

# 4 tensor (hence we have 4 variables a, b , c, x) and these tensors are coverd by 1, 2, 3, 4
a = tf.constant(1.)
b = tf.constant(2.)
c = tf.constant(3.)
x = tf.constant(4.)

# create gradient tape as tape (to describe the variety 函数的梯度(Gradient)定义为函数对各个自变量的偏导数(Partial Derivative)组成的向量)
with tf.GradientTape() as tape:
    tape.watch([x]) # add Independent variable to gradient
    y = a*x**2 + b*x + c

# calculate derivative
[dy_dx] = tape.gradient(y,[x])
print(dy_dx)
#tf.Tensor(10.0, shape=(), dtype=float32)