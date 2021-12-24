import xlrd
import pandas as pd
import requests
import random
import time

data = pd.read_excel(r'C:\Users\JK\Desktop\商品信息表.xlsx')

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

urls = data["进货链接"].dropna(axis=0, how="any", inplace=False)
print("导入完成!")
for i in urls:
    time.sleep(random.randint(1, 3))
    response = requests.get(i, headers=headers)
    print(i, response.status_code)
    if response.status_code != 200:
        print("有不存在的链接:", i)


# data = xlrd.open_workbook(r'C:\Users\JK\Desktop\商品信息表.xlsx')
# 获取所有sheet
# sheet_name = data.sheet_names()[0]

# 根据sheet索引或者名称获取sheet内容
# sheet = data.sheet_by_index(0)  # sheet索引从0开始

# 获取 第2行第2列 的值
# sheet.cell_value(2, 2)

# 获取整行和整列的值（数组）
# rows = sheet.row_values(1)  # 获取第2行内容
# cols = sheet.col_values(3)  # 获取第3列内容

# urls = [i for i in cols if i != ""]

# print(urls)




