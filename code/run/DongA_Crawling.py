# 상대경로 지정을 위한 코드
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from DataCollecting.crawling import *
import json

if __name__ == '__main__' :
    DongA_data = Crawling(1020, 513, 102) #(news_office, max_index, max_page) : #언론사 코드, 총 기사 숫자, 총 페이지 숫자 #1020, 101 * 10 + 3, 102
    DongA_data.insert(0, { "info" : {"news-office" : "동아일보", "search-keyword" : "전자발찌", "date-start" : "2008.09.29", "date-end" : "2021.10.31"}})

    for data in DongA_data[1]['news'] :
        soup = Get_soup(data['url'])
        try :
            data['txt'] = soup.find('div', {'class': 'article_txt'}).get_text()

        except AttributeError: #url로는 수집이 되지만, 페이지가 삭제된 경우에 해당하는 기사 본문 태그가 없는 경우를 대비하기 위함
            data['txt'] = 'null'

    # print(DongA_data)

    # for i in DongA_data[1]['news']:
    #     print(i)

    with open('../source/rawData/DongA_data.json', 'w', encoding="utf-8") as outfile:
        json.dump(DongA_data, outfile, indent=4, ensure_ascii = False)