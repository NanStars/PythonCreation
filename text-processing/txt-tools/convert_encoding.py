import os
import codecs
import chardet


def list_folders_files(path):
    """
返回 "⽂件夹" 和 "⽂件" 名字
    :param path: "⽂件夹"和"⽂件"所在的路径
    :return:  (list_folders, list_files)
            :list_folders: ⽂件夹
            :list_files: ⽂件
    """
    list_folders = []
    list_files = []
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            list_folders.append(file)
        else:
            list_files.append(file)
    return (list_folders, list_files)


def convert(file, in_enc="GBK", out_enc="UTF-8"):
    """
该程序⽤于将⽬录下的⽂件从指定格式转换到指定格式，默认的是GBK转到utf-8
    :param file:    ⽂件路径
    :param in_enc:  输⼊⽂件格式
    :param out_enc: 输出⽂件格式
    :return:
    """
    in_enc = in_enc.upper()
    out_enc = out_enc.upper()
    try:
        print("convert [ " + file.split('\\')[-1] + " ].....From " + in_enc + " --&gt; " + out_enc)
        f = codecs.open(file, 'r', in_enc, "ignore")
        new_content = f.read()
        codecs.open(file, 'w', out_enc).write(new_content)
    except IOError as err:
        print("I/O error: {0}".format(err))



if __name__ == "__main__":
    print('abc')
    path = r'F:\python\txt'
    (list_folders, list_files) = list_folders_files(path)
    print("Path: " + path)
    for fileName in list_files:
        filePath = path + '\\' + fileName
        with open(filePath, "rb") as f:
            data = f.read()
            a = chardet.detect(data)['encoding']
            b = 'GB2312'
            if a == b:
                convert(filePath, 'GB2312', 'UTF-8')


                # codeType = chardet.detect(data)['encoding']
