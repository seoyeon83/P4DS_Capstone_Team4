## 웹크롤링 코드

from urllib import request
import urllib
from bs4 import BeautifulSoup

def Get_soup(url) : #url을 bs4를 활용해 변환하는 과정은 꾸준히 반복되는 작업이므로, 함수를 만들어 활용
    try :   #url로는 수집이 되지만, 페이지가 삭제된 경우에 발생하는 error를 대비하기 위함
        naver = request.urlopen(url)
        naver_html = naver.read()
        soup = BeautifulSoup(naver_html, 'html.parser')

        return soup

    except urllib.error.HTTPError: #url로는 수집이 되지만, 페이지가 삭제된 경우에 발생하는 error를 대비하기 위함.
        pass


def Crawling(news_office, max_index, max_page) : #언론사 코드, 총 기사 숫자, 총 페이지 숫자
    data = [{ "news" : list(range(max_index))}] #데이터를 수집할 공간 형성
    index = 0 #data 변수 속 기사의 index

    for page in range(50, max_page) : #기사를 수집할 페이지 수만큼 반복
        soup = Get_soup('https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%A0%84%EC%9E%90%EB%B0%9C%EC%B0%8C&sort=2&photo=0&field=0&pd=3&ds=2008.09.29&de=2021.10.31&mynews=1&office_type=1&office_section_code=2&news_office_checked='+ str(news_office) +'&nso=so:r,p:from20080929to20211107,a:all&start=' + str(page) +'1')

        find_a = soup.find_all('a',{'class': 'news_tit'}) #a 태그 중, 'class' == 'news_tit'인 태그만 찾기
        find_date = soup.find_all('span', {'class': 'info'}) #span 태그 중, 'class' == 'info'인 태그만 찾기
        for i in range(len(find_a)) :
            data[0]["news"][index] = {'title' : find_a[i].get('title'), 'url' : find_a[i].get('href'), 'date' : find_date[i].get_text()}
            index += 1
            # class가 news_tit인 a 태그 안에는 title이라는 요소에 기사의 제목이 있고, href라는 요소에는 기사의 url이 들어있음.
            # 유사하게, class가 info인 span 태그는 그 기사가 올라온 날짜 텍스트를 감싸는 형태이기 때문에 get_text() 함수를 사용함.

    return data

if __name__ == '__main__' :
    #Data_crawling(1055, 10, 1)
    # data = Data_crawling(1055, 10, 1)
    # print(data)
    # for i in data :
    #     print(i)
    pass