'''
郑映慧 1619100019   2019/04/15
预处理：
将"三5.csv"、"三8.csv"、"三9.csv"三个文件分别另存为"csv(逗号分隔符文件)"："5.csv"、"8.csv"、"9.csv";
function:
    用户输入：
        1、欲分析的成绩文件；
        2、指定的输出文件夹；
        3、两个考试日期。
    程序统计这两次考试之间的成绩,绘出每个学生在指定日期期间的成绩折线图，并输出到指定文件夹，每张图片的命名皆为学生姓名；
'''

import pandas as pd
import matplotlib.pyplot as plt

def score_line_plot(filepath,output_folder):
    data=pd.read_csv(filepath,encoding='gbk')
    key=data.keys()

#输入两个考试日期，并寻找相对应的起始分析列于终止分析列
    col_begin = col_end = 0
    while (col_begin==0):
        print('''please enter the first exam date:
notice:
    you have to choose the date between these dates:''')
        print(key[5:])
        date1 = input()
        for i in range (5,len(key)):
            if date1 == key[i]:
                col_begin = i
        if col_begin == 0:
            print("error! please enter again!/n")

    while (col_end==0):
        print('''please enter the second exam date:
notice:
    you have to choose the date between these dates:''')
        print(key[5:])
        date2 = input()
        for i in range (5,len(key)):
            if date2 == key[i]:
                col_end = i
        if col_end == 0:
            print("error! please enter again!/n")

    if col_begin > col_end:
        col_begin,col_end = col_end,col_begin


#绘图并输出
    for j in range (len(data['考号'])):
        a=[]
        for i in range(col_begin,col_end+1):
            a.append(data[key[i]][j])
        plt.plot(range(col_begin,col_end+1),a,'ro-')
        plt.xlabel('exam date')
        plt.ylabel('score')
        plt.xticks(range(col_begin,col_end+1),key[col_begin:col_end+1])
        plt.ylim(0,100)
        plt.title(data['考号'][j])
        plt.legend(("score line"+' from '+date1+' to '+date2,),loc='lower left')
        plt.savefig(output_folder+'/'+data[key[3]][j]+".png")
        plt.close()


filepath = input("the path of the file which you want to analyse:")
output_folder = input("the path of the folder which you want to store output pictures in:")
score_line_plot(filepath,output_folder)