from random import randint,seed
from kriptografija import rotirajZnak

#generira ključ za kriptiranje cezarovom šifrom
#pomak je pseudoslučajni broj kako ne bi unaprijed znali što probijamo
seed()
pomak = randint(0,26)

#otvaramo datoteku sa tekstom koji želimo šifrirati
with open(r"C:\Users\Korisnik\Desktop\kripto\ulazna.txt","r",encoding="utf-8") as datoteka:
    tekst = datoteka.read().upper()

#šifriranje
šifriranitekst = ""
for znak in tekst:
    šifriranitekst += rotirajZnak(znak,pomak)

#radimo novu datoteku u koju će se spremiti šifrirani tekst
with open(r"C:\Users\Korisnik\Desktop\kripto\izlazna.txt","w",encoding="utf-8") as datoteka:
    datoteka.write(šifriranitekst)
