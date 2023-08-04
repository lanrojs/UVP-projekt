# UVP-projekt
Projektna naloga za Uvod v Programiranje 

V okviru projektne naloge bom zajel podatke o vseh zabeleženih šahovskih partijah v zadnjih petih letih s spletne strani www.chessgames.com. 

## Podatki, ki jih potrebujem za posamezno igro:
- Imeni obeh šahistov,
- Izid partije,
- Število potez,
- Leto partije,
- Otvoritev.

## Hipoteze:
- Najpogostejša otvoritev bo 1. e4,
- Najpogostejša otvoritev bo v vsakem izmed zadnjih petih let enaka,
- Med beleženimi izidi partij bo največ remijev, manj zmag belega in še manj zmag črnega,
- Povprečno število potez v zadnjih petih let se ne bo spremenilo,
- Odvisnost med otvoritvijo in številom potez je sledeča: Bolj kot je otvoritev "zaprta", večje bo povprečno število potez.

## Navodila 

V datoteki htmlregularni.py se nahaja koda za zajem podatkov s spletne strani in regularni izrazi, s katerimi sem zajel primerne dele kode. 

V datoteki json.py se nahaja koda, ki rahlo popravi zajete podatke in koda, ki pretvori JSON datoteko v CSV.

V datoteki partije.csv se nahajajo podatki: Ime belega, ime črnega, izid, število potez, leto partije, otvoritev. 

V datoteki analizapodatkov.ipynb so analizirani vsi zajeti podatki, obravnavane hipoteze, grafi. 