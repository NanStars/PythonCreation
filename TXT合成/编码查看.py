import chardet

# 以二进制的方式读取文件
f = open('F:/python/txt/韩国骚妇.txt','rb')
data = f.read()
# 去掉['encoding']可以看完整输出，这里我做了筛选，只显示encoding
print(chardet.detect(data)['encoding'])

