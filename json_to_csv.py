#==============================================================================================================================================================#
# JSON -> CSV

import json
import csv
import os

# Pretnarjeve funkcije

def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    imenik = os.path.dirname(ime_datoteke)
    if imenik:
        os.makedirs(imenik, exist_ok=True)

def zapisi_csv(slovarji, imena_polj, ime_datoteke):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(ime_datoteke, 'w', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        writer.writerows(slovarji)

with open('podatki1_popravek.json', encoding='UTF-8') as d:
    podatki1 = json.load(d)
with open('podatki2_popravek.json', encoding='UTF-8') as d:
    podatki2 = json.load(d)
with open('podatki3_popravek.json', encoding='UTF-8') as d:
    podatki3 = json.load(d)

podatki_final = podatki1 + podatki2 + podatki3
zapisi_csv(podatki_final, ['Beli', 'Črni', 'Izid', 'Število potez', 'Leto', 'Otvoritev'], 'podatki.csv')