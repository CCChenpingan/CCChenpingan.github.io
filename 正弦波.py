import matplotlib.pyplot as plt
import numpy as np
#linspace 第一个参数序列起始值，第二个参数序列结束值，第三个参数为样本数默认100
x = np.linspace(0,3*np.pi,100)#在0~3Π范围内取100个点
y = np.sin(x)#对x元素取正弦
plt.rcParams['font.sans-serif']=['SimHei']#加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.subplot(1,2,1)#将整个图像窗口分为1行2列，当前位置为1
plt.title(r'$f(x)=sin(x)$')#标题为f(x)=sin(x)
plt.plot(x,y)#x轴数据，y轴数据
#plt.show()
x1 = [t*0.375*np.pi for t in x]#将原来的x乘0.375Π给x1
y1 = np.sin(x1)#x1元素取正弦
plt.subplot(1,2,2)#将整个图像分为1行2列，当前位置为2
plt.title(r'$f(x)=sin(\omega x),\omega=\frac{3}{8}\pi$')#标题为f(x)=sin(wx),w=3/8Π
plt.plot(x,y1)#x轴数据，y轴数据
plt.show()

