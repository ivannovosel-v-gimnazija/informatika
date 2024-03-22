from kriptografija import *

with open(r"probnitekst.txt","rt",encoding="utf-8") as datoteka:
    tekst = datoteka.read().upper()

vektorAbecede = frekvencijeZnakova(tekst)

print(vektorAbecede)