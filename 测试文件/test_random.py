import random

random.seed(0)
print("Random number 1 : ", random.random())
random.seed(1)
print("Random number 11 : ", random.random())
print("-"*50)

# 生成同一个随机数
random.seed(0)
print("Random number 2 : ", random.random())
print("Random number 3 : ", random.random())
random.seed(1)
print("Random number 22 : ", random.random())
print("Random number 33 : ", random.random())
print("-"*50)
# 生成同一个随机数
random.seed(0)
print("Random number 4 : ", random.random())
print("Random number 5 : ", random.random())
print("Random number 6 : ", random.random())
random.seed(1)
print("Random number 44 : ", random.random())
print("Random number 55 : ", random.random())
print("Random number 66 : ", random.random())
