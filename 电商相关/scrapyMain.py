from selenium import webdriver
import time
from urllib.parse import unquote


# 计算机中chromedriver.exe的绝对位置
# "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(r"C:\Users\JK\Desktop\94.0.4606.61_chrome_installer-64\chrome\Chrome-bin\chromedriver.exe")
# 请求网站
driver.get("https://cbu01.alicdn.com/img/ibank/2020/777/441/23330144777_335501786.jpg")
# driver.get("https://www.bilibili.com/")
# 最大化窗口
driver.maximize_window()
# 获取当前访问的url
url = driver.current_url
print('现在的网址是:', url)
# 显示网页源码
html = driver.page_source
time.sleep(5)
# 用selenium自带的定位功能定位信息
url = driver.find_elements_by_xpath('/html/body/div[1]/div[4]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[7]/div/div/div/div[1]/div')
# 创建个空字典准备存放信息
print(url)
item = {}
# 遍历获取到的信息进行清洗
for i in url:
    item_news = {}
    # element返回的是一个对象，不能直接在xpath中使用.text方法,要在结尾使用
    number = i.find_element_by_xpath('.//span').text
    news = i.find_element_by_xpath('.//span[@class="title-content-title"]').text
    # 同理，获取属性标签的时候不能直接//href，要用.get_attribute('href')方法
    link = i.get_attribute('href')
    # url解码
    item_news[news] = unquote(link)
    item[int(number)] = item_news
# 将字典排序
item_list = sorted(item.items())
# 输出结果
for i in item_list:
    print('热度排名:', i[0], end='\t')
    print(list(i[1].keys())[0])
    print(list(i[1].values())[0])
# print('首页新闻', text)
time.sleep(3)


