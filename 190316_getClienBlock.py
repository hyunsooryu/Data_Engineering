from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup
elice_utils = EliceUtils()
class ClienCommunity:
    def __init__(self, good, short_name, title, nick_name, hit, list_time):
        self.good = good;
        self.short_name = short_name;
        self.title = title;
        self.nick_name = nick_name;
        self.hit = hit;
        self.list_time = list_time;
    def getData(self):
        print("제목: ", self.title)
        print("작성자: ", self.nick_name)
        print("좋아요: ", self.good)
        print("조회수: ", self.hit)
        print("작성 시간: ", self.list_time)
        print("작성 분류: ", self.short_name)
    
def main():
    url = "https://www.clien.net/service/group/community"
    req = urllib.request.Request(url)
    s_c = urllib.request.urlopen(url).read()
    Soup = BeautifulSoup(s_c, "html.parser")
    BOXS = Soup.find_all("div", class_ = "list_item symph_row ")
    BLOCKS = list()
    for BOX in BOXS:
        good = BOX.find("div", class_ = "list_symph view_symph").get_text().strip()
        short_name = BOX.find("span", class_ = "shortname fixed").get_text().strip()
        title = BOX.find("span", class_ = "subject_fixed").get_text().strip()
        nick_name = BOX.find("span", class_ = "nickname").get_text().strip()
        if nick_name == '':
            nick_name = 'img'
        hit = BOX.find("span", class_ = "hit").get_text().strip()
        list_time = BOX.find("span", class_  = "timestamp").get_text().strip()
        temp = ClienCommunity(good, short_name, title, nick_name, hit, list_time)
        BLOCKS.append(temp)
    for BLOCK in BLOCKS:
        BLOCK.getData()
if __name__ == "__main__":
    main()
