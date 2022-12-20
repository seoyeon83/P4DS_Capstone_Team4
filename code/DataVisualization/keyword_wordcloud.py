# 필요 라이브러리 임포트
import json 

# 언론사(SBS, 동아일보) 별 뉴스 별 상위 10 키워드 등장 횟수 카운트
def getKeywordCount(file_path) :
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)[1]['news']   # 수집 데이터에서 뉴스 데이터만 추출
        keyword = dict()    # 키워드 카운트할 딕셔너리 변수
        
        for n in data :     # 뉴스 별로 반복
            for k in n['top10_word'].keys() :   # 뉴스 데이터 속 상위 10개 단어 별로 반복
                # 키워드 카운트 변수에 개수 세기
                if k in keyword.keys() : keyword[k] += 1    
                else : keyword[k] = 1

    return keyword  # 카운트 결과 반환

# 필요 라이브러리 임포트
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 한글 폰트 사용을 위해서 세팅
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/malgun.ttf"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 딕셔너리 데이터를 받아 워드클라우드 생성
def wordcloudFromDict(data, news_office, out_file_path) :   # 데이터, 뉴스 명, 워드클라우드 저장할 파일 경로
    wc = WordCloud(font_path = font_path,     # 폰트 경로 설정
                relative_scaling=0.2,         # 크기 조절
                background_color='white',     # 배경색
                ).generate_from_frequencies(data)   # 데이터 설정

    plt.figure(figsize=(10,10))    # plot 크기 설정
    plt.imshow(wc)                 # show할 wc 설정
    plt.axis('off')                # axis 삭제

    # plot title 설정
    title = news_office + '_wordcloud'
    plt.title(title)

    plt.savefig(out_file_path + title + '.png') # plot 이미지 파일로 저장

    return None