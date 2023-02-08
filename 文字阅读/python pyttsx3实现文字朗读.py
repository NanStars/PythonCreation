import time

# 如果是windows操作系统，并且未安装pywin32, 需要安装pywin32
import pyttsx3


def talkWith(engine, line):
    """ 朗读内容 """
    engine.say(line)
    engine.runAndWait()


def talkContent(line):
    """ 朗读字符串内容 使用系统文字转语音 """

    engine = pyttsx3.init()
    # 设置朗读速度
    engine.setProperty('rate', 160)
    # 如果字符串过长 通过句号分隔 循环读取
    if len(line) > 20:
        con_list = line.split('。')
        for item in con_list:
            time.sleep(1)
            talkWith(engine, item)
    else:
        talkWith(engine, line)


# 打开名为1.txt的文件并且读取
content = open('1.txt', 'r', encoding='utf-8')
line = content.read()

talkContent(line)
