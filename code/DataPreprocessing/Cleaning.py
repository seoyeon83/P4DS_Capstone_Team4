# -*- coding: utf-8 -*-
import json

#중복 기사, 본문이 null인 기사 삭제
def Cleaning_duplicate_null(file_path, out_file_path) :
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)

        try :
            for i in range(len(data[1]['news'])) :
                if (data[1]['news'][i]['title'] == data[1]['news'][i+1]['title']) or (data[1]['news'][i]['txt'] == 'null') :
                    del data[1]['news'][i]

        except IndexError : #데이터를 삭제하면서 어쩔 수 없이 발생하는 Error 발생 방지
            pass

    with open(out_file_path, 'w', encoding="utf-8") as outfile: #또다른 json 파일에 데이터 담기
        json.dump(data, outfile, indent=4, ensure_ascii = False)

    return None

#본문 \n 삭제
def Cleaning_no_enter(file_path, out_file_path) :
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)

        for i in range(len(data[1]['news'])):
            data[1]['news'][i]['txt'] = data[1]['news'][i]['txt'].split('\n')

            # SBS에만 적용.
            #data[1]['news'][i]['txt'] = data[1]['news'][i]['txt'].split('\\xa0')
            #동아일보에만 적용.
            #data[1]['news'][i]['txt'] = data[1]['news'][i]['txt'].split('@donga.com')[0]

            txt = ''
            for j in range(len(data[1]['news'][i]['txt'])):
                if data[1]['news'][i]['txt'][j] != '':
                    txt += data[1]['news'][i]['txt'][j]
            data[1]['news'][i]['txt'] = txt

            # 동아일보에만 적용.
            #data[1]['nws'][i]['txt'] += '@donga.com'

    with open(out_file_path, 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii = False)

    return None

from konlpy.tag import Kkma

#기사의 제목과 본문 속 키워드(명사) 뽑기
def GetKeyword(file_path, out_file_path) :
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)
        delete_word = ['전자', '발찌', '전자발찌', '기자'] #동아 한정
        #기사를 크롤링할 때 전자발찌라는 키워드로 수집했기 때문에 키워드를 뽑는 과정에서 제거해줄 필요가 있음

        for i in range(len(data[1]['news'])) :
            kkma = Kkma()
            keyword = kkma.pos(data[1]['news'][i]['title']) + kkma.pos(data[1]['news'][i]['txt']) #[(word, word_type)]
            data[1]['news'][i]['keyword'] = {}
            print(i)
            for k in keyword :
                if k[0] in delete_word :
                    continue

                if k[1] == 'NNG' : #word가 명사인가?
                    if k[0] in list(data[1]['news'][i]['keyword'].keys()) :
                        data[1]['news'][i]['keyword'][k[0]] += 1
                    else :
                        data[1]['news'][i]['keyword'][k[0]] = 1

    with open(out_file_path, 'w', encoding="utf-8") as outfile:
            json.dump(data, outfile, indent=4, ensure_ascii = False)

    return None



