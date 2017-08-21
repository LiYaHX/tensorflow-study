# coding=utf-8
import tensorflow as tf

if __name__ == '__main__':
    # 声明一个常量节点
    node1 = tf.constant(2.3, dtype=tf.float32)
    # 自动识别为tf.float32
    node2 = tf.constant(4.1)
    print(node1, node2)
