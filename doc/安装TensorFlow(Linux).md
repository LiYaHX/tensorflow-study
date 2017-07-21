原文[参见这里](https://www.tensorflow.org/install/),由于电脑系统是Ubuntu，这里只关注Ubuntu下的安装，其他系统环境请参考原文

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [到底安装哪个版本](#到底安装哪个版本)
	- [仅使用CPU的TensorFlow](#仅使用cpu的tensorflow)
	- [有GPU支持的TensorFlow](#有gpu支持的tensorflow)
		- [GPU支持的前提要求](#gpu支持的前提要求)
- [开始安装TensorFlow](#开始安装tensorflow)
	- [安装pip和virtualenv](#安装pip和virtualenv)
	- [创建virtualenv环境](#创建virtualenv环境)
	- [激活virtualenv环境](#激活virtualenv环境)
	- [安装TensorFlow](#安装tensorflow)
- [校验TensorFlow是否安装好了](#校验tensorflow是否安装好了)

<!-- /TOC -->

# 到底安装哪个版本
## 仅使用CPU的TensorFlow
如果电脑上没有NVIDIA的GPU就只能安装这个版本了，官方推荐就算在你电脑上有NVIDIA的GPU时，也先安装这个版本，因为它安装比较快、比较容易。这个安装方式请直接看`开始安装TensorFlow`
## 有GPU支持的TensorFlow
既然人家提供了GPU支持，我电脑又支持，那就看看这个吧。如果电脑支持，这个版本将会显著提升TensorFlow的运行效率。好，暂且相信下，让我试试。
### GPU支持的前提要求
这一段比较长，嫌麻烦可以先跳过，等需要的时候再搞。要让GPU支持有用，咱要安装下面的东西：
- `CUDA® Toolkit 8.0` 参见[NVIDIA的文档](http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4VZnqTJ2A),说的比较多。

  - `CUDA`是`NVIDIA`搞的一个并行计算和模型的平台，类似提供了一个sdk能方便的使用GPU的并行计算能力，可以实现混合编程（CPU串行计算和GPU并行计算），串行计算使用CPU，并行计算加载到GPU运行.
  - 要使用`CUDA`电脑要满足下面几点：

    - 支持`CUDA`的GPU, 可以去[这里](https://developer.nvidia.com/cuda-gpus)看下你的GPU在不在这个列表里
    ``` shell
    使用下面的命令可以查看当前电脑上的GPU型号，然后去上面的网站查询
    $ lspci| grep -i nvidia
    $ 01:00.0 3D controller: NVIDIA Corporation GM107M [GeForce GTX 960M] (rev ff)
    ```
    - 在支持列表的Linux系统，并且安装有合适的`gcc compiler`和`toolchain`，这个要求参见原文中的表格，这里不列出
    ``` shell
    下面命令查看Linux系统信息
    $ uname -m && cat /etc/*release
    $ x86_64
    $ DISTRIB_ID=Ubuntu
    $ DISTRIB_RELEASE=16.04

    下面命令查看gcc版本
    $ gcc --version
    $ gcc (Ubuntu 5.4.0-6ubuntu1~16.04.4) 5.4.0 20160609

    下面命令查看Kernel header版本
    $ uname -r
    $ 4.4.0-83-generic
    ```
    - 从[这里](https://developer.nvidia.com/cuda-downloads)下载`NVIDIA CUDA Toolkit`，这个包好大（2GB）。按照下载页面的说明安装就好。
    ``` shell
    $ sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
    更新安装cuda
    $ sudo apt update
    $ sudo apt install cuda
    安装patch
    $ sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-cublas-performance-update_8.0.61-1_amd64.deb

    没完呢，完事后还要手动设置一些环境变量
    PATH中需要包含/usr/local/cuda-8.0/bin
    $ vi ~/.bashrc
    添加下面几行
    $ # For cuda(Tensorflow)
    $ export PATH=$PATH:/usr/local/cuda-8.0/bin
    $ export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH
    应用更新
    $ source ~/.bashrc
    ```
  - 我电脑是`960M`的，看了下[配置](https://www.geforce.com/hardware/notebook-gpus/geforce-gtx-960m/specifications),妈妈呀640个`CUDA`核心，好像很厉害的样子。
- 安装`CUDA Toolkit 8.0`对应的GPU驱动。从[这里](http://www.nvidia.com/drivers)去下载GPU驱动，需要使用375版本的，不能使用378版本的，[看这里](http://www.nvidia.com/object/gpu-accelerated-applications-tensorflow-installation.html)
![image](http://note.youdao.com/yws/public/resource/07ae14b0f86fe50712936496b0e506d5/xmlnote/WEBRESOURCE9e6a2903651ed1511b7b450b1fb2dd22/13203)
    ``` shell
    使用下面的命令可以打开nvidia的设置页面，激活Nvidia GPU
    $ nvidia-settings
    使用下面的命令可以查看驱动版本，没有代表GPU没工作
    $ cat /proc/driver/nvidia/version
    $ NVRM version: NVIDIA UNIX x86_64 Kernel Module  375.66  Mon May  1 15:29:16 PDT 2017
    $ GCC version:  gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4)
    编译个demo验证下GPU好使不
    $ cd /usr/local/cuda-8.0/samples/5_Simulations/nbody
    $ sudo make
    $ ./nbody
    ```
- `cuDNN v5.1` `Nvidia`搞的一个GPU加速的深度学习，支持一堆深度学习框架（Caffe, Caffe2, TensorFlow, Theano, Torch等）
    ``` shell
    解压下载的压缩包
    $ tar -xzvf cudnn-8.0-linux-x64-v5.1.tgz
    复制安装
    $ sudo cp cuda/include/cudnn.h /usr/local/cuda/include
    $ sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64
    $ sudo chmod a+r /usr/local/cuda/include/cudnn.h /usr/local/cuda/lib64/libcudnn*
    ```
- `libcupti-dev`，一个`NVIDIA CUDA Profile Tools Interface`，貌似对后续性能评估有好处，先安装了。
  ``` shell
  $ sudo apt install libcupti-dev
  ```
# 开始安装TensorFlow
官方提供下面几种安装方式：
- `virtualenv` : 提供一个虚拟的python环境，官方推荐，就他了
- `"native" pip`: 直接安装到系统中，其他用户可以直接访问，不用像虚拟环境里那样先要激活或者切换。
- `Docker`: 一个用户的虚拟环境，之前接触过，没仔细了解，只知道会模拟用户环境。
- `Anaconda`: 社区支持
## 安装pip和virtualenv
``` shell
python 2.7
$ sudo apt-get install python-pip python-dev python-virtualenv
python 3.x
sudo apt-get install python3-pip python3-dev python-virtualenv
```
## 创建virtualenv环境
``` shell
python 2.7
$ virtualenv --system-site-packages ~/tensorflow
python 3.x
$ virtualenv --system-site-packages -p python3 ~/tensorflow
```
> `~/tensorflow`是virtualenv环境的根目录
## 激活virtualenv环境
``` shell
$ source ~/tensorflow/bin/activate
激活或命令行会变成这样的
(tensorflow)$
```
## 安装TensorFlow
``` shell
 (tensorflow)$ pip install --upgrade tensorflow      # for Python 2.7
 (tensorflow)$ pip3 install --upgrade tensorflow     # for Python 3.n
 我当然选这个啦，好不容易把GPU支持搞定 -_-!
 6.0MB/s的下载速度，感人
 (tensorflow)$ pip install --upgrade tensorflow-gpu  # for Python 2.7 and GPU
 (tensorflow)$ pip3 install --upgrade tensorflow-gpu # for Python 3.n and GPU
```

# 校验TensorFlow是否安装好了
写上一小段`TensorFlow`的代码来验证是否正常：
``` shell
(tensorflow)$ python
>>> import tensorflow as tf
>>> hello = tf.constant('Hello, TensorFlow!')
>>> sess = tf.Session()
我把这个敲回车的时候会有GPU的一堆log出现，看来是启用啦，哇咔咔

2017-07-20 23:30:55.935026: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.1 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 23:30:55.935045: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 23:30:55.935051: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 23:30:55.935073: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 23:30:55.935078: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
2017-07-20 23:30:56.017168: I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:893] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
2017-07-20 23:30:56.017638: I tensorflow/core/common_runtime/gpu/gpu_device.cc:940] Found device 0 with properties:
name: GeForce GTX 960M
major: 5 minor: 0 memoryClockRate (GHz) 1.176
pciBusID 0000:01:00.0
Total memory: 1.96GiB
Free memory: 1.50GiB
2017-07-20 23:30:56.017653: I tensorflow/core/common_runtime/gpu/gpu_device.cc:961] DMA: 0
2017-07-20 23:30:56.017676: I tensorflow/core/common_runtime/gpu/gpu_device.cc:971] 0:   Y
2017-07-20 23:30:56.017687: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1030] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX 960M, pci bus id: 0000:01:00.0)

>>> print(sess.run(hello))
Hello, TensorFlow!
```

啊哈，安装成功，开始使用啦
