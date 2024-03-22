from kriptografija import kriptirajZnakAfino, moduloInverz

print("Upiši parametre za afinu šifru")
a = int(input("Upiši faktor A: "))
while moduloInverz(a,27) == 0:
    print("Faktor A koji ste unesli nema inverz za duljinu abecede od 27 znakova.")
    a = int(input("Upiši faktor A: "))
b = int(input("Upiši faktor B: "))
tekst = input("Upiši poruku koju želiš šifrirati: ").upper()

#šifriranje
šifriranitekst = ""
for znak in tekst:
    šifriranitekst += kriptirajZnakAfino(znak,a,b)

#radimo novu datoteku u koju će se spremiti šifrirani tekst
with open(r"C:\Users\nemoh\Desktop\kripto\kriptirano.txt","w",encoding="utf-8") as datoteka:
    datoteka.write(šifriranitekst)
