"""
data:表示协议
image/jpg:数据类型
编码方式：base64
最后部分就是编码后的数据，获取图片就是利用这个部分
运行后无法打开图片一般原因：
1.数据加密了（还有一层没解码）
2.编码不是base64
3.解码时数据中包括了“data:image/jpeg;base64,"这段
4.数据中有url编码中的换行符，去除在解码
"""
import base64

scr = input("")
image_data = scr.split(',')[1]
# 去除数据中的”data:image/jpeg;base64,"这段
image = base64.b64decode(image_data)
# 解码
with open('33.jpeg', 'wb') as f:
    # 写入33.jpeg文件
    f.write(image)
