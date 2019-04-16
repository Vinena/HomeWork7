'''
郑映慧 1619100019   2019/04/15
预处理：
将"三5.csv"、"三8.csv"、"三9.csv"三个文件分别另存为"csv(逗号分隔符文件)"："5.csv"、"8.csv"、"9.csv";
function:
    读取"5.csv"、"8.csv"、"9.csv"三个存储成绩的csv文件；
    利用循环，将5、8、9班的每个学生的成绩折线图分别输出到文件夹"三5"、"三8"、"三9"。
    折线图要求：
    1、纵坐标（y轴）是分数，横坐标是每一次的考试（日期）
    2、纵坐标的显示范围是0到100
    3、图片标题是学生学号，保存出来的文件名是学生姓名
'''

'''
5.cvs:
key==['考号', '0学校', '学校代码', '姓名', '性别', '9.08', '9.15', '9.29', '月考', '10.27',
       '11.14', '12.15', '12.31', '1.05', '1.1', '上平均', '3.13', '3.23', '月考2',
       '4.13', '4.26']
'''

import pandas as pd
import matplotlib.pyplot as plt

def score_line_plot(filename,output_folder):
    data=pd.read_csv("E:/University/study/2018-2019/python/homework/8/"+filename,encoding='gbk')
    key=data.keys()
    for j in range (len(data['考号'])):
        a=[]
        for i in range(5,len(key)):
            a.append(data[key[i]][j])
        plt.plot(range(len(key)-5),a,'ro-')
        plt.xlabel('exam date')
        plt.ylabel('score')
        plt.xticks(range(len(key)-5),key[5:])
        plt.ylim(0,100)
        plt.title(data['考号'][j])
        plt.legend(("score line",),loc='lower left')
        plt.savefig("E:/University/study/2018-2019/python/homework/8/"+output_folder+'/'+data[key[3]][j]+".png")
        plt.close()

score_line_plot('5.csv','三5')
score_line_plot('8.csv','三8')
score_line_plot('9.csv','三9')