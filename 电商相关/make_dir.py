# 创建100个文件夹，每个文件夹下有一个叫 链接地址 的TXT文件

import os

for i in range(267, 350):
    path = r"C:\Users\JK\Desktop\电商资料\上新251\LY{}".format(i)
    path = path.strip()
    isExists = os.path.exists(path)
    print(path)
    if not isExists:
        os.makedirs(path)
