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


### 2 预备知识
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

```python
#一些基本操作
#一维张量
x = torch.arange(4)
tensor([0, 1, 2, 3])
#引用元素
x[3]
tensor([3])
#长度和形状
len(x)
x.shape
#矩阵的建立
A = torch.arange(20).reshape(5, 4)
A.T  #转置矩阵
#矩阵的运算
A + B
A * B #注意这是按元素乘法
a + A #矩阵和常量相加为所有元素与矩阵元素相加
a * A
#降维
A_sum_axis0 = A.sum(axis=0) #轴0在输出形状中消失（按列求和）
#非降维求和
sum_A = A.sum(axis=1, keepdims=True) #求和后仍保持两个轴，不会去掉y轴，只是y轴为1
tensor([[ 6.],
        [22.],
        [38.],
        [54.],
        [70.]])
#可以进行 A/sum_A

A.cumsum(axis=0) #累加矩阵
torch.dot(x, y) #向量点积
torch.mv(A, x) #矩阵向量乘法
torch.mm(A, B) #矩阵矩阵乘法
u = torch.tensor([3.0, -4.0])
torch.norm(u) #L2范数，矩阵的范数为所有元素相加后开根号
torch.abs(u).sum() #L1范数
```
**2.4 导数和微积分**

亚导数：

例如f(x)=|x|，x<0导数为-1，X>0导数为1，x=0导数在-1到1之间取任意值。

注意矩阵与导数的结合。

文档中更新了绘制函数图像的模版matlab_test.py

**2.5 自动微分**

笔记记录在dx_dy.py文件中

### 3 线性神经网络

**3.1 线性回归**
**3.2 从零开始的线性回归**

linear regression文件展示了一个线性回归的实例

**3.3 线性回归的简洁实现**

**3.4 softmax回归**

**3.5 从零开始的softmax回归** 
**3.6 softmax回归的简洁实现**

一些问题：

图一
<img src="屏幕截图 2025-05-04 202222.png" alt="屏幕截图 2025-05-04 202222.png" style="zoom:20%;" />


图二
<img src="屏幕截图 2025-05-04 202130.png" alt="屏幕截图 2025-05-04 202130.png" style="zoom:20%;" />

图一是损失函数的实现，图二是损失函数的定义，好像这两个有些不同？求问学长

一些琐碎的知识


```python
titles = [true +'\n' + pred for true, pred in zip(trues, preds)]
```

**`zip(trues, preds)`**

- 将两个列表 `trues`（真实标签）和 `preds`（预测标签）逐元素配对。

**列表推导式**

- 对每一对 `(true, pred)`，生成字符串 `true + '\n' + pred`。
- `'\n'` 是换行符，使得最终显示时标签分两行排列。
