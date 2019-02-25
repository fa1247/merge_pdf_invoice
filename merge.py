import os
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter

print("将需要转换的文件夹拖入命令行 按回车（默认为此文件所在目录）")
workpath = input()
if workpath == '':
    workpath = os.getcwd()
output = os.path.join(workpath,"mergepdf.pdf")
filelist = []

files = os.listdir(workpath)

for file in files:
    if file.split('.')[-1] in ['pdf', 'PDF']:
        filelist.append(os.path.join(workpath, file))

filenum = len(filelist)

print("共找到%d个pdf文件" %filenum)
 
writer = PdfFileWriter()  #实例化写类

for i in range(filenum):
    pageobj = PdfFileReader(filelist[i]).getPage(0)
    if i%2 == 0:
        blankpage = writer.addBlankPage(610,810)
        blankpage.mergeTranslatedPage(pageobj,0,410)
    else:
        blankpage.mergeTranslatedPage(pageobj,0,0)
    
writer.removeLinks() # 移除交互链接,部分发票pdf文件在位移后会有图章重复的情况,需要移除.
writer.write(open(output,'wb')) # 写入新的文件,完成合并.

print("转换成功 输出文件",output)
