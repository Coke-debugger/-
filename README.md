安装深度学习环境：

遇到的问题（以备后用）：

1.安装conda时没有安装其默认路径安装，导致后来命令提示符无法在系统中调用，解决方法：

找到安装conda的文件夹，找到conda.exe和scripts的安装路径并添加到系统中，具体添加方法是找到高级系统设置，找到环境变量的第二个path添加路径。

2.安装d2l报错：subprocess-exited-with-error:

原因可能是版本不兼容，解决方案：

```python
pip install d2l==0.16.5
```
相关资料网站：

https://github.com/d2l-ai

[《动手学深度学习》 — 动手学深度学习 2.0.0 documentation](http://zh-v2.d2l.ai/)



**2.1 数据操作及其实现**




```python
[1:3,1:]
#表示选择第一、二行，以及列编号1之后的内容
[::3.::2]
#表示跳选，例如选择第0行、第3行，第0列、第2列
```

课后习题讨论：

1.运行本节中的代码。将本节中的条件语句`X == Y`更改为`X < Y`或`X > Y`，然后看看你可以得到什么样的张量：

2.用其他形状（例如三维张量）替换广播机制中按元素操作的两个张量。结果是否与预期相同？

```python
x = torch.tensor([1.0, 2, 4, 8])
y = torch.tensor([2, 2, 2, 2])
print(x>y)

a = torch.arange(6).reshape((2, 3, 1))
b = torch.arange(4).reshape((2, 1, 2))
print(a)
print(b)
print(a+b)
```

运行结果：

```python
tensor([False, False,  True,  True])
tensor([[[0],
         [1],
         [2]],

        [[3],
         [4],
         [5]]])
tensor([[[0, 1]],

        [[2, 3]]])
tensor([[[0, 1],
         [1, 2],
         [2, 3]],

        [[5, 6],
         [6, 7],
         [7, 8]]])
```

分析广播机制：对于两个格式不同的张量，会通过复制的方式实现对齐，然后再进行相应的加减运算。

**2.2 数据预处理**

课后习题讨论：

创建包含更多行和列的原始数据集。

1. 删除缺失值最多的列。
2. 将预处理后的数据集转换为张量格式。

```python
import torch
import os
import pandas as pd
#os.makedirs参数解析（从左向右）
#name：路径名称
#mode：目录权限，默认参数即可
#exist_ok表示如果已经存在目录是否报错，True则不报错
os.makedirs(os.path.join('..', 'data_test'), exist_ok=True)
#os.path.join表示路径拼接
#'..'为代码文件所在目录
#data_test为要拼接的部分
#house_tiny.csv为文件名
data_file = os.path.join('..', 'data_test', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('ID,name,score,gender\n')  # 列名
    f.write('1,Lihua,3.7,male\n')  # 每行表示一个数据样本
    f.write('2,NA,NA,female\n')
    f.write('4,NA,3.3,male\n')
    f.write('7,NA,4.3,male\n')
    
#
data = pd.read_csv(data_file)
print(data)
#删除缺失值最多的列
df =  data.drop('name', axis=1)
print(df)
#数据预处理（用平均值填充缺失的gpa）
inputs = df.iloc[:, 0:2]
inputs = inputs.fillna(inputs.mean())
print(inputs)

#转化为张量
X = torch.tensor(inputs.to_numpy(dtype=float))
print(X)
```

重点总结：对于缺失值采用删除法和插值法两种方法，看情况使用。

注意本练习中的数据创建和读取方法

**2.3 线性代数**
