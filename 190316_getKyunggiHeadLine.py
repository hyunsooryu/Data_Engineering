from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

elice_utils = EliceUtils()

class BLOCK: #기사를 담아낼 BOX
    def __init__(self, title, summary, reporter, date):
        self.date = date
        self.title = title
        self.summary = summary
        self.reporter = reporter
    def getData(self):
        print("DATE : ", self.date)
        print("TITLE : ", self.title)
        print("SUMMARY : ", self.summary)
        print("REPORTER: ", self.reporter)


def main(): #MAIN 함수
    url = "http://www.kyeonggi.com/?mod=news&act=articleList&view_type=S&sc_code=1439458030" #자료를 가지고 올 URL
    req = urllib.request.Request(url) #REQUEST 정보 객체
    sc = urllib.request.urlopen(url).read() #읽은 URL 소스
    Soup = BeautifulSoup(sc, "html.parser") #BEAUTIFULSOUP으로 재생산 
    BLOCKS = list()
    BOXS = Soup.find_all("div", class_ = "list-block data-article-list")
    for BOX in BOXS:
        title = BOX.find("div", class_ = "list-titles").get_text().strip()
        summary = BOX.find("p", class_ = "list-summary").get_text().strip()
        date = BOX.find("div", class_ = "list-dated").get_text().split('|')[2].strip()
        reporter = BOX.find("div", class_ = "list-dated").get_text().split('|')[1].strip()
        new_block = BLOCK(title, summary, reporter, date)
        new_block.getData()
        BLOCKS.append(new_block)
if __name__ == "__main__":
    main()


