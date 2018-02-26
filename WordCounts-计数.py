def processLine(line,wordCounts):
    line = replacePunctuations(line)
    #空格替换标点符号

    words=line.split()
    #从每一行获取每个词

    for word in words:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            wordCounts[word]=1

def replacePunctuations(line):
    #标点符号替换成空格

    for ch in line:
        if ch in "~@#$%^&*()_-+=<>?/,.:;{}[]|\'""":
            line =line.replace(ch,"")
    return line

def main():
    # 用户输入一个文件名
    filename=input("Enter a filename:").strip()
    #strip为去除头尾的空格
    infile=open(filename,"r")

    #建立用于计算词频的空字典
    wordCounts={}
    for line in infile:
        processLine(line.lower(),wordCounts)
        #lower将大写字母转换成小写

    #从字典中获取数据对
    pairs=list(wordCounts.items())

    #列表中的数据对交换位置，数据对排序
    items=[[x,y]for (y,x)in pairs]
    items.sort()
main()
