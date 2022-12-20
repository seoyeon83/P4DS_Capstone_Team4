# 상대경로 지정을 위한 코드
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from DataVisualization.keyword_wordcloud import *

if __name__ == '__main__' :
    # 언론사 별 뉴스 별 상위 10 키워드 카운트
    DongA_keyword_count = getKeywordCount("../../source/preprocessedData/DongA_data_3.json")
    SBS_keyword_count = getKeywordCount("../../source/preprocessedData/SBS_data_3.json")

    # 키워드 카운트한 데이터로 워드클라우드 출력
    wordcloudFromDict(DongA_keyword_count, 'DongA', '../../plot/')
    wordcloudFromDict(SBS_keyword_count, 'SBS', '../../plot/')