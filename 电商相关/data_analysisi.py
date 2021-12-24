#!C:\Users\JK\AppData\Local\Programs\Python\Python37-32


import pandas as pd
import os

from pip._vendor.distlib.compat import raw_input

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
warehouse = os.listdir(r'C:\Users\JK\Desktop\库存分析')
warehouse_name = [warehouse[0] for file in warehouse if file.__contains__("restock")][0]

template = pd.read_csv(r'C:\Users\JK\Desktop\库存分析\商品库存模板.csv', encoding="gb2312")
workbook = pd.read_excel(r'C:\Users\JK\Desktop\库存分析\{}'.format(warehouse_name))

# print(df)
sku = template['需要关注的Sku']
skuFordeal = workbook['Fordeal SKU']

t1 = pd.DataFrame(template)
t1.set_index('需要关注的Sku', drop=True, append=False, inplace=True)
t2 = pd.DataFrame(workbook)
t2.set_index('Fordeal SKU', drop=True, append=False, inplace=True)

t3 = t1.join(t2)

t3_in_warehouse = pd.DataFrame(t3["在仓可用库存"])
t3["在仓可用库存"] = t3_in_warehouse.fillna(0)
t3_in_way = pd.DataFrame(t3["发货在途数量(非跨境)"])
t3["发货在途数量(非跨境)"] = t3_in_way.fillna(0)
t3_in_do = pd.DataFrame(t3["处理中数量（非跨境）"])
t3["处理中数量（非跨境）"] = t3_in_do.fillna(0)
# print(t3)
# need_stock = t3["固定库存"] - t3["在仓可用库存"] - t3["发货在途数量(非跨境)"] - t3["处理中数量（非跨境）"]
need_stock = t3["在仓可用库存"] + t3["发货在途数量(非跨境)"] + t3["处理中数量（非跨境）"]

need_stock = pd.DataFrame(need_stock)

# need_stock = need_stock.fillna(1000)

t3["需要进货数量"] = need_stock

data_need_stock_list = t3["需要进货数量"].tolist()
data_need_stock_list = [str(i) for i in data_need_stock_list]

data_need_notice_sku = t3.index
data_need_notice_sku = [str(i) for i in data_need_notice_sku]

data_belong_product = t3["所属商品货号"].tolist()
data_belong_product = [str(i) for i in data_belong_product]

data_prepare = t3["固定库存"].tolist()
data_prepare = [str(i) for i in data_prepare]

data_size = t3["尺码"].tolist()
data_size = [str(i) for i in data_size]


data = {
    "需要关注的Sku": data_need_notice_sku,
    "所属商品货号": data_belong_product,
    "尺码": data_size,
    # "固定库存": data_prepare,
    "库存": data_need_stock_list
        }

df = pd.DataFrame(data)

df.to_csv(r'C:\Users\JK\Desktop\库存分析\商品库存推荐发货单.csv', index=False, mode='w')

print("结束！")
# print(t3.loc[:, ["需要关注的Sku", "所属商品货号", "在仓可用库存", "固定库存", "需要进货数量"]])
# print(t3["需要关注的Sku"].tolist())

# print(sku.tolist())
# print(skuFordeal.tolist())


# 前5行信息
# print(df.head())
# 基础信息
# print(df.info())
# 总体描述
# print(df.describe())

# DataFrame中排序的方法
# df = df.sort_values(by='Count_AnimalName', ascending=False)
# 方括号写数字表示对行操作
# print(df[:5])
# 方括号写字符串表示对列操作
# print(df[:5]['Row_Labels'])

# raw_input("Press Enter key to exit.")
