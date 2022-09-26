# -*- coding: utf-8 -*
print('hello, world')

# with open("input.txt", "r") as f:  #打开文件
#     data = f.readline()  #读取文件
#     print(data)

a = 0
sp = ""
sp2 = ""


file2 = open("output.txt","w")
for line in open("input.txt"):
    #这里可以进行逻辑处理
    # print(line),
    line=line.strip('\n')
    if len(line.strip()) ==0:
        continue
    if( "作者" in line):
        a = 1
        continue
    if( "来自" in line):
        a = 1
        continue
    if(a==1):
        sp=":"
        sp2 = "\n"
    file2.write(sp+line+sp2)
    sp = ""
    sp2 = ""
    a = 0

file2.close()

# input()
print('hello, end')
