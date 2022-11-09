## 데이터 저장 상황을 보기 위한 코드

import json

file_path_SBS = "../source/SBS_data_2.json"
file_path_DongA = "../source/DongA_data_2.json"

with open(file_path_SBS, encoding='utf-8') as file:
    data = json.load(file)
    print("SBS :",len(data[1]['news']))

with open(file_path_DongA, encoding='utf-8') as file:
        data = json.load(file)
        print("DongA :", len(data[1]['news']))