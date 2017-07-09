import tensorflow as tf

str = tf.Variable("Hello TensorFlow")
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(str))
