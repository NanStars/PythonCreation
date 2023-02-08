import os


def getAllTxt():
    # 文件夹目录
    path = "F:/python/txt"
    # 得到文件夹下的所有文件名称
    files = os.listdir(path)
    txts = []
    num = 1
    # 遍历文件夹
    for file in files:
        # 构造绝对路径，"\\"，其中一个'\'为转义符
        position = path + '\\' + file
        # 输出路径
        print(position)
        # 判断文件是否是txt文档
        if file.endswith(".txt"):
            # 打开文件
            with open(position, "r", encoding='utf-8') as f:
                # 读取文件
                data = f"第{num}篇 " + f.read() + '\n\n'
                num += 1
                txts.append(data)
    # 转化为非数组类型
    txts = ''.join(txts)
    with open('./合并.txt', 'a', encoding='utf-8') as file:
        # print(txts)
        file.write(txts)


getAllTxt()
