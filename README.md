# tensorflow-study
Record the machine learning process </n>
###### DevEnv: MacOS 10.12
###### Official website: [TensorFlow](https://www.tensorflow.org/)

### Install TensorFlow

##### // 1. 修改hosts文件为默认配置（没有修改过hosts文件可跳过此步骤）

##### 2. brew更新
```
$sudo chown -R $(whoami) /usr/local
$brew update
$sudo chown root:wheel /usr/local
```

##### 3. 安装pip
```
$sudo python get-pip.py
```

##### 4. 不用MacOS自带的python。重新安装python。
```
$which python
 /usr/bin/python
$brew install python
$which python
 /usr/local/bin/python
$hash -r python
$easy_install pip
```

##### 5. 安装tensorflow
```
$pip install tensorflow
$pip install tensorflow-gpu
$pip uninstall tensorflow-gpu
```

##### Note 1:
######   a. `brew linkapps python` 命令已弃用，改用`hash -r python`
######   b. MacOS暂不支持tensorflow-gpu，因此需卸载：`pip uninstall tensorflow-gpu`
######   c. 建议看[TensorFlow](https://www.tensorflow.org/)，因为中文官网更新有延时

##### Note 2:
######   a. [一文读懂TensorFlow（附代码、学习资料）](https://mp.weixin.qq.com/s/SlitM8JToD7dN5E5Ue9wjA) ![image](https://github.com/LiYaHX/tensorflow-study/blob/master/doc/images/arc_of_tensorflow_study.jpeg)
