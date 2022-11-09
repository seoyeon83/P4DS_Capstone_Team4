## 데이터 클리닝 수행

# 상대경로 지정을 위한 코드
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from DataPreprocessing.Cleaning import *

if __name__ == '__main__' :
    Cleaning_duplicate_null('../../source/rawData/DongA_data.json', '../../source/preprocessedData/DongA_data_1.json')
    Cleaning_no_enter('../../source/preprocessedData/DongA_data_2.json', '../../source/preprocessedData/DongA_data_2.json')
    # '../data/DongA_data_1.json', 'DongA_data_keyword.json'
    GetKeyword('../../source/preprocessedData/DongA_data_2.json', '../../source/preprocessedData/DongA_data_keyword.json')

    Cleaning_duplicate_null('../../source/rawData/SBS_data.json', '../../source/preprocessedData/SBS_data_1.json')
    Cleaning_no_enter('../../source/preprocessedData/SBS_data_2.json', '../../source/preprocessedData/SBS_data_2.json')
    # '../data/SBS_data_1.json', 'SBS_data_keyword.json'
    GetKeyword('../../source/preprocessedData/SBS_data_2.json', '../../source/preprocessedData/SBS_data_keyword.json')