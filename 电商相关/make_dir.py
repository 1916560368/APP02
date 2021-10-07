# 创建100个文件夹，每个文件夹下有一个叫 链接地址 的TXT文件

import os

for i in range(100):
    path = r"C:\Users\JK\Desktop\电商资料\上新的\商品{}".format(i)
    path = path.strip()
    isExists = os.path.exists(path)
    print(path)
    if not isExists:
        os.makedirs(path)
        txtpath = path + r"\链接地址.txt"
        open(txtpath, "w")
        print(path, "创建成功")
    else:
        print(path, "已经存在")
