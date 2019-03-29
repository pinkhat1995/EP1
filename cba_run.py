import demjson
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
from tqdm import tqdm

json_name = './cba.json'

def main():
    json = list()
    for i in tqdm(range(1,27)):
        print('------page %d start--------' % i)
        html = BeautifulSoup(requests.get('https://cba.hupu.com/players/players.php?sort=%d' % i).content, 'html.parser')
        for tr in html.find_all('tr', attrs={'style':'color:#990000'}):
            td = tr.find_all('td')
            num = td[0].get_text()
            name = td[1].find('a').get_text()
            page = td[1].find('a')['href']
            team = td[2].get_text()
            height = td[3].get_text().split('CM',1)[0]
            weight = td[4].get_text().split('KG',1)[0]
            pos = td[5].get_text()
            birth = td[6].get_text() #(td[6].get_text() is not '') and datetime.strptime(td[6].get_text(),'%Y年%m月%d日') or datetime.strftime('1900年1月1日','%Y年%m月%d日')
            msg = {
                'Num': num,
                'Name': name,
                'Team': team,
                'Height': height,
                'Weight': weight,
                'Pos': pos,
                'Brith': birth,
                'Page':page
            }
            json.append(msg)
            print(msg)
        for tr in html.find_all('tr', attrs={'style':'color: #990000'}):
            td = tr.find_all('td')
            num = td[0].get_text()
            name = td[1].find('a').get_text()
            page = td[1].find('a')['href']
            team = td[2].get_text()
            height = td[3].get_text().split('CM',1)[0]
            weight = td[4].get_text().split('KG',1)[0]
            pos = td[5].get_text()
            birth = td[6].get_text() #(td[6].get_text() is not '') and datetime.strptime(td[6].get_text(),'%Y年%m月%d日') or datetime.strftime('1900年1月1日','%Y年%m月%d日')
            msg = {
                'Num': num,
                'Name': name,
                'Team': team,
                'Height': height,
                'Weight': weight,
                'Pos': pos,
                'Brith': birth,
                'Page':page
            }
            json.append(msg)
            print(msg)
        print('------page %d compeleted, sleep 20s------' % i)
        time.sleep(20)
    print('encoding...')
    demjson.encode_to_file(json_name,json)
           
        
        
        
        




if __name__ == '__main__':
    main()