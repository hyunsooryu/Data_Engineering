import urllib.request
from bs4 import BeautifulSoup

def main():
    url = "http://sports.donga.com/Enter?p=1&c=02"
    req = urllib.request.Request(url)
    sc = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sc, "html.parser")

    boxs = soup.select(".cont_info > .tit")
    href_boxs = []
    for box in boxs:
        href_boxs.append(box.find("a")["href"])
    
    for href_box in href_boxs:
        new_sc = urllib.request.urlopen(href_box)
        soup = BeautifulSoup(new_sc, "html.parser")
        print(soup)

    
    

if __name__ == "__main__":
    main()
