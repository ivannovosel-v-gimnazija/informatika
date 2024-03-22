from kriptografija import *

#otvaramo datoteku sa dosta teksta na ciljanom jeziku
#ovo radimo kako bi zračunali tablicu frekvencija ako nije poznato unaprijed
with open(r"C:\Users\Korisnik\Desktop\kripto\probni tekst na hrvatskom.txt","r",encoding="utf-8") as datoteka:
    tekst = datoteka.read().upper()
#normalna frekvencija hrvatskog jezika
vektorAbecede = frekvencijeZnakova(tekst)

#otvaramo datoteku sa šifriranim tekstom
with open(r"C:\Users\Korisnik\Desktop\kripto\izlazna.txt","r",encoding="utf-8") as datoteka:
    tekst = datoteka.read().upper()
#frekvencija znakova u šifriranom tekstu
vektorŠifre = frekvencijeZnakova(tekst)

#dešifriranje frekvencijskom analizom
#prvo tražimo ključ
produkti = [] #stavljamo produkte u listu kako bi kasnije našli najvećeg
for pomak in range(27):
    rotirajVektor(vektorŠifre)
    produkti.append(skalarniProdukt(vektorAbecede,vektorŠifre))
#index najvećeg produkta +1 je naš ključ
pomak = produkti.index(max(produkti))+1

dešifrirani = ""
for znak in tekst:
    dešifrirani += rotirajZnak(znak,-pomak)

#radimo novu datoteku u koju će se spremiti dešifrirani tekst
with open(r"C:\Users\Korisnik\Desktop\kripto\dekriptirano2.txt","w",encoding="utf-8") as datoteka:
    datoteka.write(dešifrirani)
