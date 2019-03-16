import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import re

class movie:
    def __init__(self, name, genre, day_on, runningTime, nation, netizenScore, repoterScore, Conductor, Actor,preStory):
        self.netizenScore = netizenScore
        self.day_on = day_on
        self.runningTime = runningTime
        self.nation = nation
        self.netizenScore = netizenScore
        self.repoterScore = repoterScore
        self.Conductor = Conductor
        self.Actor = Actor
        self.preStory = preStory
        self.name = name
        self.genre = genre
    
    def getData(self):
        print("----------------------------------------------------------------------------------------------")
        print("제목 : ", self.name)
        print("장르 : ", self.genre)
        print("개봉일 : ", self.day_on)
        print("국가 : ", self.nation)
        print("상영시간 : ", self.runningTime)
        print("네티즌 평점 :", self.netizenScore)
        print("기자단 평점 :", self.repoterScore)
        print("배우 :", self.Actor)
        print("줄거리: ", self.preStory)
        print("----------------------------------------------------------------------------------------------")

def main():
    #-----------------------------------------------------------WEBDRIVER-------------------------------------------------------------
    #-----------------------------------------------------------WEBDRIVER-------------------------------------------------------------
    #-----------------------------------------------------------WEBDRIVER-------------------------------------------------------------
    #-----------------------------------------------------------WEBDRIVER-------------------------------------------------------------
    data = input("알고싶은 영화를 입력하세요: ")
    driver = webdriver.Chrome("C:\driver/chromedriver")
    #driver.implicitly_wait(3)
    driver.get("https://movie.naver.com/")
    
    #class - > ipt_tx_srch
    driver.find_element_by_id('ipt_tx_srch').send_keys(data)
    driver.find_element_by_class_name('btn_srch').click()
    #class - > btn_srch
    driver.find_element_by_class_name('result_thumb').click()

    target = driver.page_source
    Soup = BeautifulSoup(target, "html.parser")
    #-----------------------------------------------------------BEAUTIFUL_SOUP--------------------------------------------------------
    #-----------------------------------------------------------BEAUTIFUL_SOUP--------------------------------------------------------
    #-----------------------------------------------------------BEAUTIFUL_SOUP--------------------------------------------------------
    #-----------------------------------------------------------BEAUTIFUL_SOUP--------------------------------------------------------
    #-----------------------------------------------------------BEAUTIFUL_SOUP--------------------------------------------------------
    name = data
    P = Soup.find("dl", class_ = "info_spec").find("p").get_text().strip()
    real_list = re.findall('\w+', P)
    #print(real_list)
    day_on = real_list[-4] + "-" + real_list[-3] + "-" + real_list[-2];
    runningTime = real_list[-5]
    nation = real_list[-6]
    genre = ", ".join(real_list[0:-6])
    #print(genre)   
    Conductor = Soup.select('.info_spec > dd')[1].text
    #print(Conductor)
    Actor = Soup.select('.info_spec > dd')[2].text[:-3]
    #print(Actor)
    preStory = Soup.find('p', class_ = "con_tx").get_text().strip()
    #print(preStory)
    #NET
    ScoreArea = Soup.find("div", class_ = "score_area").get_text().strip()
   # print(ScoreArea)
    t2 = "\d[.]\d+"
    score_data = re.findall(t2, ScoreArea)
    #print(score_data)
    netizenScore = score_data[0]
    repoterScore = score_data[1]

    ANS = movie(name, genre,day_on, runningTime,nation, netizenScore,repoterScore,Conductor, Actor,preStory)
    ANS.getData()
if __name__ == "__main__":
    main()
