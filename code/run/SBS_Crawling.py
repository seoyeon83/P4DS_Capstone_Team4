# 상대경로 지정을 위한 코드
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from DataCollecting.crawling import *
import json

if __name__ == '__main__' :
    SBS_data = Crawling(1055, 8, 127) #(news_office, max_index, max_page) : #언론사 코드, 총 기사 숫자, 총 페이지 숫자 #1055, 126 * 10 + 8, 126 //// 268, 126
    SBS_data.insert(0, { "info" : {"news-office" : "SBS", "search-keyword" : "전자발찌", "date-start" : "2008.09.29", "date-end" : "2021.10.31"}})

    for data in SBS_data[1]['news'] :
        soup = Get_soup(data['url'])
        try :
            data['txt'] = soup.find('div', {'class': 'text_area'}).get_text()
        except AttributeError: #url로는 수집이 되지만, 페이지가 삭제된 경우에 해당하는 기사 본문 태그가 없는 경우를 대비하기 위함
            data['txt'] = 'null'

    # print(SBS_data)
    # print(len(SBS_data[1]['news']))
    # for i in SBS_data[1]['news']:
    #     print(i)

    with open('../source/rawData/SBS_data.json', 'w', encoding="utf-8") as outfile:
        json.dump(SBS_data, outfile, indent=4, ensure_ascii = False)
