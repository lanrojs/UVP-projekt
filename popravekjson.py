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


#============================================================================================================================================================#
# Popravljanje JSON-datotek



def score_match(score_str : str):
    if score_str not in ['1-0', '0-1', '&#189;-&#189;']:
        print('Prišlo je do napake!')
    elif score_str == '1-0':
        return 'Beli zmaga'
    elif score_str == '0-1':
        return 'Črni zmaga'
    else:
        return 'Remi'

def json_edit(json_file : str, new_json_file : str):
    with open(json_file, encoding='UTF-8') as d:
        json_text = d.read()
    dict_list = json.loads(json_text)
    out = []
    for dict in dict_list:
        temp_dict = {}
        temp_dict['Beli'] = dict['names'].split(' vs ')[0]
        temp_dict['Črni'] = dict['names'].split(' vs ')[1]
        temp_dict['Izid'] = score_match(dict['score'])
        temp_dict['Število potez'] = int(dict['moves'])
        temp_dict['Leto'] = int(dict['year'])
        temp_dict['Otvoritev'] = dict['opening'].strip()
        out.append(temp_dict)
    zapisi_json(out, new_json_file)

json_edit('podatki1.json', 'podatki1_popravek.json')
json_edit('podatki2.json', 'podatki2_popravek.json')
json_edit('podatki3.json', 'podatki3_popravek.json')