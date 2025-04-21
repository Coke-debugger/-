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



**数据操作及其实现**

![](file:///D:/download1/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250421123053.jpg)



