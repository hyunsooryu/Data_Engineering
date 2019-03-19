import urllib.request
from bs4 import BeautifulSoup
  

def main():
    print("-----------------------LOTTO WELCOME----------------------------")
    clientNum = int(input("로또 기록 열람을 최근 순으로 몇회까지 보시겠습니까?"))
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%A1%9C%EB%98%90&oquery=850%ED%9A%8C%EB%A1%9C%EB%98%90&tqi=U5teispVuFdsstd7NDNsssssthZ-128777"
    req = urllib.request.Request(url)
    sc = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sc, "html.parser")
    current = int(soup.select_one("._lotto-btn-current > em").get_text()[:-1])
    while clientNum > 0:
        new_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%A1%9C%EB%98%90+" + str(current) + "%ED%9A%8C&oquery=%EB%A1%9C%EB%98%90&tqi=U5te9dpVuFdsstcccBKssssssbG-108338"
        new_sc = urllib.request.urlopen(new_url)
        new_soup = BeautifulSoup(new_sc, "html.parser")
        lottoNumData = new_soup.select(".num_box > span")
        lottoDayData = new_soup.select("._lotto-btn-current > span")[0].text
        print(lottoDayData + " 제 " + str(current) + "회 로또번호: ", end = "")
        for num in lottoNumData:
            print(num.get_text().strip(), end = " ")
        print("\n")
        clientNum -= 1
        current -= 1
    


if __name__ == "__main__":
    main()