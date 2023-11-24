import random
import re
import requests
from time import sleep
from bs4 import BeautifulSoup
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary 

import rcv_year

chrome_path = '/Users/kuroto9610/Desktop/Programming/scraping/chromedriver'

d_list = []
def list_of_horse():
    #あとで年単位で取得するときに作る
    ####################################################
    print("欲しいレース情報のidを入力してください")
    # print("まず最初に何年から何年まで取得するか入力してください")
    # from_year,to_year= rcv_year.rcv_year_range()[0:2]

    print("場所コード「東京:05、京都:08、福島:03」")
    race_id = int(input("レースの日付＋場所コード＋回数＋日数:"))
    # for year in range(int(from_year), int(to_year)):
    #########################################################

    for i in range(1,13):            #指定した場所・日程のその日のレースの１２回分の出馬表URLの取得
        print("R",i)
        url = "https://race.netkeiba.com/race/shutuba.html?race_id={0}{1}&rf=race_submenu"
        
        judge_len = str(i)
        if len(judge_len) == 1:
            round = judge_len.zfill(2)
        
        elif len(judge_len) > 1: 
            round = i

        target_url = url.format(race_id,round)
        print(target_url)

        options = Options()
        options.add_argument('--incognito')
        driver = webdriver.Chrome(executable_path=chrome_path, options=options)
        driver.get(target_url)
        driver.set_script_timeout(10) #JavaScript実行までの待機時間

        html = driver.page_source.encode('utf-8')
        sleep(random.randint(1,4))
        soup = BeautifulSoup(html, 'html.parser')
        [tag.extract() for tag in soup(string='\n')] #改行コード削除

        Shutuba_list_table = soup.find("div",class_="RaceTableArea")
        table = Shutuba_list_table.find("table",class_="Shutuba_Table")
        # column_name = table.find("thead")

        Shutuba_lists = table.find_all("tr",class_="HorseList")
        for Shutuba_list in Shutuba_lists:
            waku,horse_num,horse_name,sex_age,sekiryou,jockey,trainer,weight,odds,popular\
            = Shutuba_list.find_all("td")[:2] + Shutuba_list.find_all("td")[4:12]
            #↓取得内容確認用
            #print(waku.text,horse_num.text,horse_name.text,sex_age.text,sekiryou.text,jockey.text,trainer.text,weight.text,odds.text,popular.text)
        
            

            Shutuba_dic = {"枠":waku.text,
                            "馬番":horse_num.text,
                            "馬名":horse_name.text,
                            "性齢":sex_age.text,
                            "斥量":sekiryou.text,
                            "騎手":jockey.text,
                            "厩舎":trainer.text,
                            "馬体重":weight.text,
                            "オッズ":odds.text,
                            "人気":popular.text}
            print("######################")
            pprint(Shutuba_dic)

        driver.quit()
    



list_of_horse()