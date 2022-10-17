'''
문1) iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
    <조건1> iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
    <조건2> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
    <조건3> 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후  5번 칼럼으로 색상 적용 
'''

import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('C:\\ITWILL\\4_Python-II\\data\\iris.csv')
print(iris.info())

plt.scatter(iris['Sepal.Length'],iris['Petal.Length'], c='r', marker='o')
plt.show()

species = iris['Species']
species.unique()
# ['setosa', 'versicolor', 'virginica']

len(species)

cdata = []
for s in species:
    if s == 'setosa':
        cdata.append(3)
    elif s == 'versicolor':
        cdata.append(4)
    else:
        cdata.append(5)
        

plt.scatter(iris['Sepal.Length'],
            iris['Petal.Length'],
            c = cdata, marker = 'o')










