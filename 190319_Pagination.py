import urllib.request
from bs4 import BeautifulSoup

def main():
    titles  = []
    for page in range(0, 5):
        url = "http://sports.donga.com/Enter?p=" + str(page * 20 + 1) + "&c=02"
        req = urllib.request.Request(url)
        sc = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(sc,"html.parser")
        sub_titles = soup.select(".cont_info > .tit")
        #sub_titles = soup.find_all("span", class_ = "tit")
        for sub_title in sub_titles:
            titles.append(sub_title.text)
            #titles.append(sub_title.get_text().strip())
    
    print(titles)

    



if __name__ == "__main__":
    main()