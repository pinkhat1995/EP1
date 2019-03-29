import demjson
import requests
from bs4 import BeautifulSoup
import re
import time

hrefs = [
    'https://nba.hupu.com/players/rockets',
    'https://nba.hupu.com/players/spurs',
    'https://nba.hupu.com/players/pelicans',
    'https://nba.hupu.com/players/grizzlies',
    'https://nba.hupu.com/players/mavericks',
    'https://nba.hupu.com/players/warriors',
    'https://nba.hupu.com/players/clippers',
    'https://nba.hupu.com/players/kings',
    'https://nba.hupu.com/players/lakers',
    'https://nba.hupu.com/players/suns',
    'https://nba.hupu.com/players/nuggets',
    'https://nba.hupu.com/players/blazers',
    'https://nba.hupu.com/players/jazz',
    'https://nba.hupu.com/players/thunder',
    'https://nba.hupu.com/players/timberwolves',
    'https://nba.hupu.com/players/raptors',
    'https://nba.hupu.com/players/76ers',
    'https://nba.hupu.com/players/celtics',
    'https://nba.hupu.com/players/nets',
    'https://nba.hupu.com/players/knicks',
    'https://nba.hupu.com/players/magic',
    'https://nba.hupu.com/players/heat',
    'https://nba.hupu.com/players/hornets',
    'https://nba.hupu.com/players/wizards',
    'https://nba.hupu.com/players/hawks',
    'https://nba.hupu.com/players/bucks',
    'https://nba.hupu.com/players/pacers',
    'https://nba.hupu.com/players/pistons',
    'https://nba.hupu.com/players/bulls',
    'https://nba.hupu.com/players/cavaliers',
]

if __name__ == '__main__':
    l = []
    for href in hrefs:
        print(href)
        html = BeautifulSoup(requests.get(href).text, 'html.parser')
        trs = html.select('table.players_table tbody tr')[1:]
        for tr in trs:
            tmp = {
                'Name': tr.select('td.left p b')[0].text,
                'Height': float(re.search('([\d\.]+)米*',tr.select('td:nth-of-type(5)')[0].text).group(1)),
                'Weight': float(re.search('([\d\.]+)公斤*', tr.select('td:nth-of-type(6)')[0].text).group(1)),
            }
            print(tmp['Name'])
            l.append(tmp)
        time.sleep(2)
    open('nba.json','w').write(demjson.encode(l))
