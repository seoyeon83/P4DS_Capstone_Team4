## 기사별 키워드 중요도 추출

# 상대경로 지정을 위한 코드
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from DataPreprocessing.Keyword import *

if __name__ == '__main__' :
    GetKeyword('../../source/preprocessedData/SBS_data_2.json', '../../source/preprocessedData/SBS_data_keyword.json')
    GetTFIDF("../../source/preprocessedData/SBS_data_keyword.json", "../../source/preprocessedData/SBS_Keyword_100.csv")
    GetTop10Word("../../source/preprocessedData/SBS_Keyword_100.csv", "../../source/preprocessedData/SBS_data_2.json", "SBS_data_3.json")

    GetKeyword('../../source/preprocessedData/DongA_data_2.json', '../../source/preprocessedData/DongA_data_keyword.json')
    GetTFIDF("../../source/preprocessedData/DongA_data_keyword.json", "../../source/preprocessedData/DongA_Keyword_100.csv")
    GetTop10Word("../../source/preprocessedData/DongA_Keyword_100.csv", "../../source/preprocessedData/DongA_data_2.json", "DongA_data_3.json")