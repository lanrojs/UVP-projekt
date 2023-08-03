import requests as req
import re
import json
import os


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
}


def kraja_html(max_st_strani : int, st_let : int):
    for i in range(st_let):
        for result in ['0-1', '1-0', '1/2-1/2']:
            for pg_num in range(max_st_strani):
                response1 = req.get(
                    f"https://www.chessgames.com/perl/chess.pl?page={pg_num}&yearcomp=exactly&year={2023 - i}&playercomp=either&pid=&player=&pid2=&player2=&movescomp=le&moves=39&opening=&eco=&result={result}",
                    headers=headers
                    )
                if response1.status_code == 200:
                    print(f'{2023 - i}: {result}, page: {pg_num} pt. 1')
                    with open(f'html_code.html', 'a', encoding='UTF-8') as d:
                        d.write(response1.text)
                else:
                    print('ERROR: ' + f'{2023 - i}: {result}, page: {pg_num}')
                #============================================================================================================================================#
                response2 = req.get(
                    f"https://www.chessgames.com/perl/chess.pl?page={pg_num}&yearcomp=exactly&year={2023 - i}&playercomp=either&pid=&player=&pid2=&player2=&movescomp=ge&moves=40&opening=&eco=&result={result}",
                    headers=headers
                    )
                if response2.status_code == 200:
                    print(f'{2023 - i}: {result}, page: {pg_num} pt. 2')
                    with open(f'html_code.html', 'a', encoding='UTF-8') as d:
                        d.write(response2.text)
                else:
                    print('ERROR: ' + f'{2023 - i}: {result}, page: {pg_num}')
    



kraja_html(500, 5)



# Pretnarjeve funkcije
def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def zapisi_json(objekt, ime_datoteke):
    '''Iz danega objekta ustvari JSON datoteko.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as json_datoteka:
        json.dump(objekt, json_datoteka, indent=4, ensure_ascii=False)


game_sample = re.compile(
    r'''<font face='verdana,arial,helvetica' size=-1>\d+?\.&nbsp;<a href="/perl/chessgame\?gid=\d+?">(?P<names>.+?)</a></font></td>.*?''' # name vs name
    r'''<font face='verdana,arial,helvetica' size=-1>(?P<score>[01&#89;\-]{1,6}?-[01&#89;\-]{1,6}?)</font></td><td align=RIGHT>.*?''' # Score
    r'''<font face='verdana,arial,helvetica' size=-1>(?P<moves>\d{1,3}?)</font></td><td align=RIGHT>.*?''' # Moves
    r'''<font face='verdana,arial,helvetica' size=-1>(?P<year>\d{4,4})</font></td><td><font face='verdana,arial,helvetica' size=-1>.*?''' # Year
    r'''<a href="/perl/chessopening\?eco=.+?">[a-zA-Z0-9]{0,4}?</a>(?P<opening>.+?)</font></font></td>''', # Opening
    flags=re.DOTALL
    )

def parse_html_to_json(html_file : str, json_file : str):
    out = []
    counter = 1
    with open(html_file, encoding='UTF-8') as d:
        html_code = d.read()
    for game in game_sample.finditer(html_code):
        print(game.groupdict())
        out.append(game.groupdict())
        print(counter)
        counter += 1
    zapisi_json(out, json_file)

parse_html_to_json('htmlcode1.html', 'podatki1.json')
parse_html_to_json('htmlcode2.html', 'podatki2.json')
parse_html_to_json('htmlcode3.html', 'podatki3.json')