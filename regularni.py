import re
import json
import os

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