# -*- coding: utf-8 -*-

import numpy as np # 다차원배열, 선형대수 연산 
import matplotlib.pyplot as plt

# 1. 알려진 두 집단 x,y 산점도 시각화 
plt.scatter(1.2, 1.1) # A 집단
plt.scatter(1.0, 1.0)
plt.scatter(1.8, 0.8) # B 집단 
plt.scatter(2, 0.9)

plt.scatter(1.6, 0.85, color='r') # 분류대상 
plt.show()

# 2. DATA 생성과 함수 정의 
p1 = [1.2, 1.1] # A 집단 
p2 = [1.0, 1.0]
p3 = [1.8, 0.8] # B 집단
p4 = [2, 0.9]
category = ['A','A','B','B'] # 알려진 집단 분류범주(Y변수)
p5 = [1.6, 0.85] # 분류대상 

# data 생성 함수 정의
def data_set():
    # 선형대수 연산 : numpy형 변환 : 리스트를 어레이로 변경하여 선형대수를 하려는 작업
    know_group = np.array([p1, p2, p3, p4]) # 알려진 집단 - 2차원 
    not_know_group = np.array(p5) # 알려지지 않은 집단 - 1차원 
    class_category = np.array(category) # 정답(분류범주)
    return know_group,not_know_group,class_category 


know, not_know, cate = data_set()

know.shape # (4, 2)
not_know.shape # (2,)
cate.shape #  (4,)







