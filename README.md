# index-of
Download ebook from [index-of.es](http://index-of.es) or [index-of.co.uk](http://index-of.co.uk)

## Available commands
```
q -> quit                                                                                                                                                                                   
p -> previous                                                                                                                                                                               
n -> next                                                                                                                                                                                   
c -> clear                                                                                                                                                                                  
d -> download                                                                                                                                                                               
s -> set domain                                                                                                                                                                             
h -> help
```

## bad commands
![bad next](https://i.ibb.co/bJd8fDc/output.gif)

Menggunakan  `n` command pada file

![bad_download](https://i.ibb.co/G3s0kkD/bad-download.gif)

Menggunakan `d` command pada folder

## set downloaded dir
![downloadDir](https://i.ibb.co/jgtR7mq/download-dir.gif)

ketik `vim index.py` lalu ubah value dari variable outdir

## Installation
```
[sudo] apt install python3 git
[sudo] python3 -m pip install mechanize bs4 requests
git clone https://github.com/r3duc3/index-of
```

## Run it
```
cd index-of
python3 index.py
```

## Requirements
- Python3x
- git
- module python:
  - requests
  - mechanize
  - bs4
