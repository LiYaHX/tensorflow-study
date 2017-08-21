# coding=utf-8
import tensorflow as tf

if __name__ == '__main__':
    # 声明一个常量节点
    node1 = tf.constant(2.3, dtype=tf.float32)
    # 自动识别为tf.float32
    node2 = tf.constant(4.1)

    # 声明一个操作节点
    nodeAdd = tf.add(node1, node2)
    # 这样也可以
    nodeAdd2 = node1 + node2
    print nodeAdd
    sess = tf.Session()
    print sess.run(nodeAdd)
    print sess.run(nodeAdd2)

    add_and_triple = nodeAdd * 3.
    print sess.run(add_and_triple)
