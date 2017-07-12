#### Run mnist_softmax.py

  a. Download MNIST data for input（Preparation）；
  ```
  $python
  >>>from tensorflow.examples.tutorials.mnist import input_data
  >>>mnist = input_data.read_data_sets("MNIST_data/", one_hot=True) #Option operate
  >>>exit()
  ```
  b. Run mnist_softmax.py
  ```
  $python mnist_softmax.py
  ```
  c. Output
  ```
  0.9209
  ```
  ###### Note: MNIST(Modified National Institute of Standards and Technology)
