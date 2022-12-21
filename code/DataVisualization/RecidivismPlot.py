import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df1 = pd.read_csv("../../source/preprocessedData/연도별 성폭력 전자감독대상자 재범건수.csv", encoding='utf-8')

#그림 사이즈, 바 굵기 조정
fig, ax = plt.subplots(figsize=(12, 6))
w = 0.25

# 연도가 13개이므로 0, 1 ... , 13 위치를 기준으로 삼음
index = np.arange(13)

# 각 연도별로 3개 샵의 bar를 순서대로 나타내는 과정, 각 그래프틑 0.25의 간격을 두고 그려짐
b1 = plt.bar(index - w, df1['총인원'], width = w,  color='red', label='총인원')
b2 = plt.bar(index, df1['전체재범건수'], width = w, color='blue', label='전체재범건수')
b3 = plt.bar(index + w, df1['성폭력재범건수'], width = w, color='green', label='성폭력재범건수')

# x축 위치를 정 가운데로 조정하고, x축의 텍스트를 연도 정보와 매칭
plt.xticks(index, df1['연도'])
plt.legend()
plt.savefig('../../plot/성폭력 전자감독대상자 재범 분포 plot.png') # plot 이미지 파일로 저장
plt.show()