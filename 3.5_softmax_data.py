import torch
import torchvision
from torch.utils import data
from torchvision import transforms
from d2l import torch as d2l
import matplotlib.pyplot as plt
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
d2l.use_svg_display()

# 通过ToTensor实例将图像数据从PIL类型变换成32位浮点数格式，
# 并除以255使得所有像素的数值均在0～1之间
trans = transforms.ToTensor()
mnist_train = torchvision.datasets.FashionMNIST(
    root="../data", train=True, transform=trans, download=True)
mnist_test = torchvision.datasets.FashionMNIST(
    root="../data", train=False, transform=trans, download=True)

print(len(mnist_train), len(mnist_test)) #前者为训练集数，后者是测试集数
print(mnist_train[0][0].shape) #查看数据的格式

#以下函数用于在数字标签索引及其文本名称之间进行转换
def get_fashion_mnist_labels(labels):  #@save
    """返回Fashion-MNIST数据集的文本标签"""
    text_labels = ['t-shirt', 'trouser', 'pullover', 'dress', 'coat',
                   'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']
    return [text_labels[int(i)] for i in labels]

#以下函数用于可视化样本
def show_images(imgs, num_rows, num_cols, titles=None, scale=1.5):  #@save
    """绘制图像列表"""
    #num_cols和num_rows分别对应图像的列、行数，scale为放大比例，figsize设置整个画布的尺寸
    figsize = (num_cols * scale, num_rows * scale)
    #创建子图
    _, axes = d2l.plt.subplots(num_rows, num_cols, figsize=figsize)
    #将子图（subplots）的轴（axes）数组从多维展平为一维
    axes = axes.flatten()
    #同时遍历子图轴（axes）和图像列表（imgs）;zip(axes, imgs)：将 axes 和 imgs 按顺序配对（例如 (ax1, img1), (ax2, img2), ...）。
    #enumerate()：添加索引 i，用于后续标题的匹配。
    for i, (ax, img) in enumerate(zip(axes, imgs)):
        if torch.is_tensor(img):#判断图像是否为 PyTorch 张量
        #如果是张量，需调用 .numpy() 转换为 NumPy 数组（matplotlib 需要 NumPy 或 PIL 格式）。其他情况（如 PIL 图像或 NumPy 数组），直接调用 ax.imshow()。
            # 图片张量
            ax.imshow(img.numpy())
        else:
            # PIL图片
            ax.imshow(img)
        #隐藏当前子图的 x 轴和 y 轴（包括刻度线和标签）
        ax.axes.get_xaxis().set_visible(False)
        ax.axes.get_yaxis().set_visible(False)
        if titles: #如果传入了标题列表 titles，则为当前子图设置标题
            ax.set_title(titles[i])
    return axes

X, y = next(iter(data.DataLoader(mnist_train, batch_size=18))) #加载和读取一小部分（batch_size=18）数据集
show_images(X.reshape(18, 28, 28), 2, 9, titles=get_fashion_mnist_labels(y))
plt.show()

#读取小批量数据
batch_size = 256
def get_dataloader_workers():  #@save
    """使用4个进程来读取数据"""
    return 4

train_iter = data.DataLoader(mnist_train, batch_size, shuffle=True,
                             num_workers=get_dataloader_workers())

timer = d2l.Timer()
#查看数据读取所需的时间
for X, y in train_iter:
    continue
f'{timer.stop():.2f} sec'

#整合所有组件
#定义load_data_fashion_mnist函数，用于获取和读取Fashion-MNIST数据集。
#返回训练集和验证集的数据迭代器，且可以接受一个可选参数resize，用来将图像大小调整为另一种形状。
def load_data_fashion_mnist(batch_size, resize=None):  #@save
    """下载Fashion-MNIST数据集，然后将其加载到内存中"""
    trans = [transforms.ToTensor()]
    if resize:
        trans.insert(0, transforms.Resize(resize))
    trans = transforms.Compose(trans)
    mnist_train = torchvision.datasets.FashionMNIST(
        root="../data", train=True, transform=trans, download=True)
    mnist_test = torchvision.datasets.FashionMNIST(
        root="../data", train=False, transform=trans, download=True)
    return (data.DataLoader(mnist_train, batch_size, shuffle=True,
                            num_workers=get_dataloader_workers()),
            data.DataLoader(mnist_test, batch_size, shuffle=False,
                            num_workers=get_dataloader_workers()))
    
#指定resize参数来测试load_data_fashion_mnist函数的图像大小调整功能
#resize 参数的功能
#作用：指定是否将原始图像（默认 28×28 像素）调整为其他尺寸。
#类型：通常是一个整数或元组（如 resize=64 或 resize=(64, 64)）。
#如果传入整数（如 64），图像将按比例缩放为 (64, 64)。
#如果传入元组（如 (64, 80)），图像将调整为指定尺寸。
#默认值：None（不调整尺寸，保持原始 28×28）
train_iter, test_iter = load_data_fashion_mnist(32, resize=64)
for X, y in train_iter:
    print(X.shape, X.dtype, y.shape, y.dtype)
    break