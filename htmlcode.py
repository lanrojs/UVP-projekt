import requests as req

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