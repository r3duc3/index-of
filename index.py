#!/usr/bin/python3

import mechanize, os
from requests import get
from bs4 import BeautifulSoup as be

br = mechanize.Browser()
br.set_handle_redirect(False)
br.set_handle_robots(False)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36')]

u = ''
comm = (
        'q', 'p', 'n', 'c', 'd', 's', 'h'
        )
width = os.get_terminal_size().columns
outdir = '/sdcard/Documents/' # tempat file terunduh

w = tuple([chr(27)+'[1;0m'] + list(chr(27)+'[1;3'+str(x)+'m' for x in range(1,7)))

def h():
    print(w[0]+'''q -> quit
p -> previous
n -> next
c -> clear
d -> download
s -> set domain
h -> help''')

def url():
    global u
    ex = ('es', 'co.uk')
    if u == '':
        try:
            u = 'http://index-of.'+ex[int(input('\n'.join(f'{ex.index(x)+1}. {x}' for x in ex)+'\n> '))-1]+'/'
            c()
        except:
            exit()
    return u

def size(num, suffix='B'):
    for unit in ['','K','M','G','T','P','E','Z']:
        if abs(num) < 1024.0:
            return "%04.2f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.2f%s%s" % (num, 'Y', suffix)

def q():
    exit()

def s():
    global u; u = ''
    c()

def listx():
    c()
    ls = {}
    r = be(str(br.open(u).read()), 'html.parser').find_all('div', attrs={'class' : "buybox-content"})[2].pre.select('a')[2:]
    for x in r:
        ls.update({x.text : x['href']}) if x.text != '' else None

    print('\n'.join(f'{w[4]}{list(ls.keys()).index(x)+1}. {w[6]}{x}' for x in ls))
    return ls

def n():
    global u
    x = listx()
    try:
        y = input(w[1]+'> ')
        if list(x.keys())[int(y)-1] == 'Parent Directory':
            p()
        else:
            u += x[list(x.keys())[int(y)-1]]
    except:
        return
    finally:
        c()

def p():
    global u
    u = 'http://'+''.join(x+'/' for x in u.split('/')[:-2][2:]) if len(u.split('/')[:-2][2:]) != 0 else ''

def d():
    x = listx()
    try:
        y = input(w[1]+'> ')
        c()
        r = br.open(u+x[list(x.keys())[int(y)-1]])
        tot = int(r._headers.get("Content-Length"))
        print(f'{w[0]}{list(x.keys())[int(y)-1]} {size(tot)}')
        uwu = input('Lanjut[y/n]: ')
        if uwu == 'n':
            return
        if not os.path.exists(outdir):
            os.mkdir(outdir)

        out = open(outdir+list(x.keys())[int(y)-1], 'wb')
        chunksize = 16384
        bit = 0
        while True:
            chunk = r.read(chunksize)
            out.write(chunk)
            bit += len(chunk)
            if not chunk:
                out.close()
                break
            print(f'\r{" "*(width)}', end='')
            print(f'\r{w[2]}Downloading {w[3]}{size(bit)} {w[5]}({bit*1.0/tot:.2%})', end='', flush=True)

        print(f'\n{w[5]}Downloaded: {w[4]}{outdir}{list(x.keys())[int(y)-1]}')

    except Exception as ex:
        print(ex)
        return

def c():
    os.system('clear')
    print(w[1]+r'''__________
< index-of >
 ----------
  \     .    _  .
   \    |\_|/__/|
       / / \/ \  \
      /__|O||O|__ \
     |/_ \_/\_/ _\ |
     | | (____) | ||
     \/\___/\__/  //
     (_/         ||
      |          ||
      |          ||\
       \        //_/
        \______//
       __ || __||
      (____(____)
      ''')

c()

while True:
    x = input(f'{w[6]}{url()}\n{w[2]}>>>{w[0]} ')
    if x in comm:
        exec(x+'()')
