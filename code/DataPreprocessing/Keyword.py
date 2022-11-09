# -*- coding: utf-8 -*-
from konlpy.tag import Kkma
import json

#기사의 제목과 본문 속 키워드(명사) 뽑기
def GetKeyword(file_path, out_file_path) :
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)
        delete_word = ['전자', '발찌', '전자발찌', '기자']
        #기사를 크롤링할 때 전자발찌라는 키워드로 수집했고, 기자는 뉴스 기사 특성상 자주 나오지만 의미없는 단어이기 때문에 제거

        for i in range(len(data[1]['news'])) :
            kkma = Kkma()
            keyword = kkma.pos(data[1]['news'][i]['title']) + kkma.pos(data[1]['news'][i]['txt']) #[(word, type)]
            data[1]['news'][i]['keyword'] = {}
            print(i)
            for k in keyword :
                if k[0] in delete_word : continue #제외하는 word에 해당되면 넘기기
                if k[1] == 'NNG' : #word가 명사인가?
                    if k[0] in list(data[1]['news'][i]['keyword'].keys()) : data[1]['news'][i]['keyword'][k[0]] += 1
                    else : data[1]['news'][i]['keyword'][k[0]] = 1 #키워드의 등장 횟수가 1회 이상이면 +1, 아니면 추가

    with open(out_file_path, 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii = False)

    return None

from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import csv

#TF-IDF로 키워드별 중요도 구하기
def GetTFIDF(file_path, out_file_path) :
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)

        # 추출한 단어들을 하나의 문자열로 만들기
        corpus = []
        for i in range(len(data[1]['news'])) :
            result = ''
            corpus.append(list(data[1]['news'][i]['keyword'].keys()))
            for j in corpus[i] :
                result += ((j + ' ')*data[1]['news'][i]['keyword'][j])
            corpus[i] = result

        vect = CountVectorizer(max_features = 100)
        document_term_matrix = vect.fit_transform(corpus)

        tf = pd.DataFrame(document_term_matrix.toarray(), columns=vect.get_feature_names())
        D = len(tf)
        df = tf.astype(bool).sum(axis=0)
        idf = np.log((D+1) / (df+1)) + 1

        tfidf = tf * idf
        tfidf = tfidf / np.linalg.norm(tfidf, axis=1, keepdims=True)

        tfidf.to_csv(out_file_path, encoding="utf-8-sig")

    return None

#기사별 중요도가 높은 10개의 단어와 중요도를 데이터에 추가
def GetTop10Word(csv_file_path, json_file_path, out_file_path) : #, out_file_path
    with open(json_file_path, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        csv_data = list(csv.reader(open(csv_file_path, "r", encoding='utf-8-sig')))

        for i in range(len(json_data[1]['news'])) :
            json_data[1]['news'][i]['top10_word'] = {}

            top10 = csv_data[i+1][1:] #중요도만 있는 리스트 생성
            top10.sort(reverse=True) #내림차순 정렬
            top10 = top10[:10] #가장 높은 중요소 10가지

            for j in range(10) :
                json_data[1]['news'][i]['top10_word'][csv_data[0][csv_data[i + 1].index(top10[j])]] = float(top10[j])

    with open(out_file_path, 'w', encoding="utf-8") as outfile:
        json.dump(json_data, outfile, indent=4, ensure_ascii = False)

    return None
