import urllib.request
from bs4 import BeautifulSoup

def main():
    href_list = []
    for i in range(1, 11):
        url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS&pageIdx=" + str(i)
        req = urllib.request.Request(url)
        sc = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sc, "html.parser")

        href_boxs = soup.select(".mfn_inner > .mfn_cont")
        for box in href_boxs:
            new_url ="https://news.sbs.co.kr/" +  box["href"]
            new_sc = urllib.request.urlopen(new_url).read()
            new_soup = BeautifulSoup(new_sc, "html.parser")
            text_area = new_soup.find("div", class_ = "text_area").get_text().strip()
            print(text_area)
            if "장자연" in text_area:
                href_list.append(new_url)
        
    
    cnt = len(href_list)
    
    for i in range(0, cnt):
        print(href_list[i])
    

    
    
    



if __name__ == "__main__":
    main()