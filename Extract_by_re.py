import re
pat1 = re.compile(r".{13}-[4-9]\.[0-9]")  #利用正则匹配log中的打分行
with open("test.all","r",encoding="utf-8") as f:  #test.all文件是合并所有输出log之后的文件
data = [0]  #定义一个用于存放行索引的列表
i = 0
x = 0
for (i,line) in enumerate(f):
score = re.match(pat1,line)
if score:
print(score.group())
x = i + 3  #vina输出文件log文件中，分子名在打分行后第3行
data.append(x)
# The last element of "data" is always mol_name line index.
if i == data[-1]:
print(line)
f.close
