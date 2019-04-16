'''
郑映慧 1619100019   2019/04/16
预处理：
将"三5.csv"、"三8.csv"、"三9.csv"三个文件分别另存为"csv(逗号分隔符文件)"："5.csv"、"8.csv"、"9.csv";
function:
       计算出学生所有参与统计的考试的个人平均分，并且绘制出该班的成绩分布图（以10分为一个统计区间）
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecs

#用户输入指定文件、程序读取文件数据
filepath = input("the path of the file which you want to analyse:")
data=pd.read_csv(filepath,encoding='gbk')
key=data.keys()
nstu = len(data[key[0]])
file = codecs.open(filepath,encoding='latin1')
score = np.loadtxt(file, usecols=(range(5,len(key))),delimiter = ',', skiprows=1,unpack = True)
# print(score)

#算每个学生的平均分
ave_score = score.sum(axis=0)/(len(key)-5)
# print(ave_score)

#画频率分布直方图
times=plt.hist(ave_score,bins=range(0,110,10),align=u'mid',rwidth=0.9)
Y=times[0]
X=times[1]
print(Y)
plt.xticks(X,X)
for x,y in zip(X,Y):
       plt.text(x+5,y+0.05,'%.0f'%y,ha='center',va='bottom')
plt.show()
# bin=np.histogram(ave_score,range=(0,100))