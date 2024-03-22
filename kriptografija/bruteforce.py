from kriptografija import rotirajZnak

#otvaramo datoteku sa šifriranim tekstom
with open(r"C:\Users\Korisnik\Desktop\kripto\izlazna.txt","r",encoding="utf-8") as datoteka:
    tekst = datoteka.read().upper()
    if len(tekst) > 20:
        kratko = tekst[0:20] #ako je tekst dugačak ne treba nam cijeli

#brute force dešifriranje
#isprobat ćemo sve i vidjeti koji ključ paše
svipokušaji = []
for pomak in range(27):
    pokušaj = str(pomak)+": "
    for znak in kratko:
        pokušaj += rotirajZnak(znak,-pomak)
    svipokušaji.append(pokušaj+"\n")

#radimo novu datoteku u koju će se spremiti dešifrirani tekst
with open(r"C:\Users\Korisnik\Desktop\kripto\dekriptirano.txt","w",encoding="utf-8") as datoteka:
    datoteka.writelines(svipokušaji)
