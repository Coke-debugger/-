# Python 学习笔记

放一个速查宝典：

<img src="C:\Users\何可凡\Pictures\Screenshots\屏幕截图 2025-02-09 155402.png" alt="屏幕截图 2025-02-09 155402" style="zoom:25%;" />



1.精确计算小数

```python
import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(a+b)
```



2.复数的使用

```python
x = 1 + 2j
x.real
>>1.0
x.imag
>>2.0
```



3.科学计数法

```python
0.00005
>>5e-05
```



4.一些数学运算

除法与地板除

```python
3/2
>>1.5
3 // 2
>>1
3 // -2
>>-2
```

除法与C语言有略微不同，并非整除；地板除是取结果的向下取整



函数divmod

```python
divmod(3,2) #3为被除数，2为除数
>>(1, 1) #第一个数为为地板除结果，第二个数为余数，3=1*1+1
```

绝对值函数abs

```python
abs(-3)
>>3
abs(1+3j)
>>3.1622776601683795 #取模
```

整值函数int

```python
int('520')
520
int(3.14)
3
```

浮点数函数float

```python
float('3.14')
3.14
float(+1E6)
1000000.0
float(520)
520.0
```

复数函数complex

```python
complex('1+2j')
(1+2j)
complex('1 + 2j') #需要转换的字符串不能有空格
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    complex('1 + 2j')
ValueError: complex() arg is a malformed string
```

幂函数pow

```python
pow(2,3)
8
pow(2,3,5) #2**3%5
3
2**3
8
```



5.布尔类型

对于bool(x)

x只有为下面的情况时运算结果才可能为FALSE。

<img src="C:\Users\何可凡\Pictures\Screenshots\屏幕截图 2025-02-09 161502.png" alt="屏幕截图 2025-02-09 161502" style="zoom:80%;" />



6.逻辑运算

python的逻辑运算用and or not

and or not本身的运算结果由参数决定

<img src="C:\Users\何可凡\Pictures\Screenshots\屏幕截图 2025-02-09 162444.png" alt="屏幕截图 2025-02-09 162444" style="zoom:50%;" />

进一步解释上面的运算结果：

```python
(not 1) or (0 and 1) or (3 and 4) or (5 and 6) or (7 and 8 and 9)
>>4
```

先运算小括号里面的内容，前两个是0，不是决定算式结果的关键，影刺第三个括号是关键，and需要确定两个数字才能得到结果。



有关运算有限级：

<img src="C:\Users\何可凡\Pictures\Screenshots\屏幕截图 2025-02-11 101111.png" alt="屏幕截图 2025-02-11 101111" style="zoom:80%;" />

越往后运算顺序越靠前。



7.分支语句

if

```python
#三种基本结构
if ... :
    执行语句
else:
    执行语句
    
    
if ...  :
    执行语句
elif ...:
    执行语句
elif ...:
    执行语句
else:
    执行语句  
 
第三种：
score = 66
level = ( 'A' if 80<=score<=100 else
          'B' if 60<=score<80   else
          'C')
print(level)
>>B
即为：
语句 A if condition else 语句 B
condition成立则执行前者，否则执行后者
```



8.循环语句



实例：

```python
while True:
    word = input("主人，我可以退出循环了吗？")
    if word == "可以！":
        break
```

while--else结构：

```python
day = 1
while day <= 7:
    answer = input("今天你有好好学习吗？")
    if(answer == "有"):
        day+=1
    else:
        break
else:
    print("你已经完成了一周的学习任务，真棒！")
```

只有while的条件不成立时，才会引发else的内容，上面的例中，只有连续输入七个有，才会打印出else的内容。



for循环语句实例：

```python
for i in range(2,10,2):
    print(i)
    
for each in "FishC":
    print(each)
```

range相关参数为头尾以及步长

in 后面的内容必须是一个序列



9.一些常用函数

print：例子如下

```python
print(i,"*",j,"=",end=" ")
```



### 列表

##### 定义与引用

```python
rhyme = [1,2,3,4,5,"上山打老虎"]
rhyme[-1]
'上山打老虎'
rhyme[0:2]
[1, 2]
rhyme[0:3]
[1, 2, 3]
rhyme[:3]
[1, 2, 3]
rhyme[:5]
[1, 2, 3, 4, 5]
rhyme[::2]
[1, 3, 5]
rhyme[::-2]
['上山打老虎', 4, 2]
```



列表的操作：

```python
heros = ["钢铁侠","绿巨人"]
heros.append("黑寡妇")
heros
['钢铁侠', '绿巨人', '黑寡妇']
heros.extend(["鹰眼","灭霸","雷神"])
heros
['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '灭霸', '雷神']
s[len(s):]=[6]
s
[1, 2, 3, 4, 5, 6]
s[len(s):]=[7,8,9]
s
[1, 2, 3, 4, 5, 6, 7, 8, 9]
s=[1,3,4,5]
s.insert(1,2)
s
[1, 2, 3, 4, 5]
s.insert(0,0)
s
[0, 1, 2, 3, 4, 5]
s.insert(len(s),6)
s
[0, 1, 2, 3, 4, 5, 6]
heros.remove("灭霸")
heros
['钢铁侠', '绿巨人', '黑寡妇', '鹰眼', '雷神']
heros.pop(2)
'黑寡妇'
heros
['钢铁侠', '绿巨人', '鹰眼', '雷神']
```



列表常见的替换元素方法：

```python
heros = ["蜘蛛侠","绿巨人","黑寡妇","鹰眼","灭霸","雷神"]
heros[4] = "钢铁侠"
heros
['蜘蛛侠', '绿巨人', '黑寡妇', '鹰眼', '钢铁侠', '雷神']
heros.reverse()
heros
['雷神', '钢铁侠', '鹰眼', '黑寡妇', '绿巨人', '蜘蛛侠']
heros[3:] = ["武松","林冲","李逵"]
heros
['雷神', '钢铁侠', '鹰眼', '武松', '林冲', '李逵']
```



列表排序与逆置

```python
nums = [3, 1, 9, 6, 8, 3, 5, 3]
nums.sort()
nums
[1, 3, 3, 3, 5, 6, 8, 9]
nums.reverse()
nums
[9, 8, 6, 5, 3, 3, 3, 1]

#另一种逆置方法
nums = [3, 1, 9, 6, 8, 3, 5, 3]
nums.sort(reverse=True)
nums
[9, 8, 6, 5, 3, 3, 3, 1]
```



一些列表常用操作：

```python
nums = [3, 1, 9, 6, 8, 3, 5, 3]
nums.count(3) #查找3的个数
3
nums.index(3) #查找第一个出现3的位置下标
0
nums.index(3,1,7) #以此类推，查找1到7范围内的
4
#下面是两种复制操作
nums_copy1 = nums.copy()
nums_copy1
[9, 8, 6, 5, 3, 3, 3, 1]
nums_copy2 = nums[:]
nums_copy2
[9, 8, 6, 5, 3, 3, 3, 1]
```



列表的运算

```python
s = [1, 2, 3]
t = [4, 5, 6]
s + t
[1, 2, 3, 4, 5, 6]
s * 3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```



二维列表

```python
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
for i in matrix:
    for each in i:
        print(each, end=' ')
    print()
#打印结果：
1 2 3 
4 5 6 
7 8 9 

matrix[0][0] #单个元素的引用
1
```



二维列表的初始化

```python
#正确的方法
A = [0] * 3
for i in range(3):
    A[i] = [0] * 3
    
#错误的方法
B = [[0] * 3] * 3
#这种方法实际上只是重复了列表引用，B[0]和B[1]实际上是一个东西
```



python不同于C语言，x = y的操作并不是拷贝相应的值，而是将两个变量用同一个指针联系到一起。

而真正拷贝的操作见下：

```python
#对于单层列表
#操作1：
y = x.copy()
#操作2：
y = x[:]

#对于嵌套列表
import copy
y = copy.deepcopy(x)
```



列表推导式：

```python
#两个简单的例子
oho = [1, 2, 3, 4, 5]
oho = [i*2 for i in oho]
oho
[2, 4, 6, 8, 10]

code = [ord(c) for c in "FishC"]
code
[70, 105, 115, 104, 67]

#嵌套列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in matrix]
col2
[2, 5, 8]

col1 = [col for row in matrix for col in row]
col1
[1, 2, 3, 4, 5, 6, 7, 8, 9]

#初始化列表
S = [[0]*3 for i in range(3)]
S[1][1] = 1
S
[[0, 0, 0], [0, 1, 0], [0, 0, 0]]

#添加了条件判断的列表恒等式， 先处理for内容，再处理if内容
even = [i for i in range(10) if i%2 == 0]
even
[0, 2, 4, 6, 8]

#其他类型
z = [x+y for x in "FishC" for y in "FishC"]
z
['FF', 'Fi', 'Fs', 'Fh', 'FC', 'iF', 'ii', 'is', 'ih', 'iC', 'sF', 'si', 'ss', 'sh', 'sC', 'hF', 'hi', 'hs', 'hh', 'hC', 'CF', 'Ci', 'Cs', 'Ch', 'CC']
```

你好哈哈
