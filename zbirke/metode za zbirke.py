# %% [markdown]
# # Ugrađene metode za pojedine zbirke
# 
# U ovoj bilježnici se nalaze primjeri koje demonstriraju kako se koristi koja od ugrađenih metoda za pojedine zbirke. Ideja ovog dokumenta je da dobijete pregled toga što unutar Pythona postoji. Neke od ovih metoda ćemo koristiti češće pa ćete ih vjerojatno i zapamtiti, ali **nije nužno pamtiti sve metode napamet**. Ovaj pregled je tu da znate što tražiti jednom kad vam zatreba.
# 
# Pod svakim od naslova naći ćete primjere za svaku od zbirki, grupirane po namjeni. Svaki podnaslov za namjene je inicijalno pritvoren (vidjet ćete **>** s lijeve strane naslova).
# 
# > Kliknite na **>** znak kako bi ste vidjeli primjere unutra!
# 
# Ako želite brže naći metode iskoristite opciju **Outline** iz glavnog izbornika iznad - to će prikazati tablicu sadržaja za cijelu bilježnicu.

# %% [markdown]
# ## Zbirka string

# %% [markdown]
# ### Razdvajanje stringova na dijelove + spajanje nazad
# 
# Osim uobičajenog `split()` koji često koristimo za razdvajanje postoji i njegov pandan `join()` koji stringove spaja nazad, ali postoji i nekoliko različitih verzija split metode za različite situacije.

# %%
primjer = "Nešto za\trazdvajanje je tu\n"

# metoda split() razdvaja string po nekom znaku i sprema odvojene stringove u listu.
# ako ne ostavimo nikakav argument split() će razdvojiti po bilo kojem praznom znaku (space,tab i sl.)
primjer.split()


# %%
# malo detaljniji primjeri...
popis = "prvi,drugi,treći,četvrti,peti,šesti"

# možemo definirati po kojem znaku se lomi
print(f"Lista ako polomimo po zarezu: {popis.split(',')}")
print(f"Lista ako polomimo po slovu i: {popis.split('i')}")

# možemo reći i do koliko dijelova se lomi
# ovo se čita kao "polomi string dok ne nađeš 3 zareza i onda stani sa razdvajanjem"
print(f"Lista ako polomimo do 3 zareza: {popis.split(',',3)}")

# postoji i metoda rsplit() koja radi jednako, ali počinje od kraja stringa (od desna na lijevo)
print(f"Lista ako polomimo s rsplit() po zarezu: {popis.rsplit(',',3)}")
# uočite da rsplit() ne mijenja redoslijed elemenata u listi

# splitlines() specifično razdvaja po znakovima za novi red \n
popis = "prvi\ndrugi\ntreći\nčetvrti\npeti\nšesti"

print(f"Ako imamo puno redova: {popis.splitlines()}")
print(f"Ako imamo puno redova: {popis.splitlines(keepends=True)}") #možemo i zadržati \n u stringovima

# %%
# join() radi obratno od split() metode
# on kao argument prima neku zbirku (tj. nešto po čemu može iterirati)
# spaja sve elemente koje dobije pomoću stringa na kojem se metoda pozove

popis = "prvi,drugi,treći,četvrti,peti,šesti".split(",")

" ".join(popis)

# %%
# string na kojem pozivamo join() služi kao "ljepilo"
popis = "prvi,drugi,treći,četvrti,peti,šesti".split(",")

print(f"Ako spajamo sa žnj dobije se: {'žnj'.join(popis)}")
print(f"Ako ne želimo išta između stavi se prazni string: {''.join(popis)}")

# %%
# join() spaja stringove tako da ovo neće raditi
lista = [1,2,3,4,5]
",".join(lista)

# %%
# ali ovakve konstrukcije hoće jer svaki element pretvaramo sa str()

lista = [1,2,3,4,5]
spojeno = ",".join(str(broj) for broj in lista)
print(f"Iz liste: {spojeno}")

spojeno = ",".join(str(i) for i in range(1,6))
print(f"Može i sa range(): {spojeno}")

# %%
# partition() je specifična metoda koja vraća ntorku (tuple kao rezultat)
# zadaje joj se znak za razdvajanje i ona vraća ono što je ostalo prije tog znaka, sam znak i ono poslije

primjer = "3.4+6.5"
print(f"Partition je zgodan kad imamo 2 stvari odvojene separatorom. Npr. {primjer} postane {primjer.partition('+')}")
primjer = "3.4+6.5+2.5443"
print(f"Ne baš toliko zgodan ako ih je više (onda je bolji split()). Npr. {primjer} postane {primjer.partition('+')}")
# postoji i rpartition koji radi s kontra strane
print(f"Isto to može i sa rpartition(). Npr. {primjer} postane {primjer.rpartition('+')}")

# %% [markdown]
# ### Pretraživanje sadržaja stringa
# 
# Pomoću ovih metoda možemo saznati na kojoj poziciji se nalaze pojedini znakovi, ili drugi stringovi, u stringu kojeg pretražujemo.

# %%
# metode find() i index() rade vrlo slično. osnovni argument je string koji tražimo
# obje će vratiti prvo mjesto na kojem počinje taj string

rečenica = "Ovo je nešto malo dulje. Malo dulje čisto tako imamo po čemu pretraživati."

# index i find daju isti rezultat ako nešto nađu - poziciju prvog znaka gdje traženi string počinje
print(f"Mjesto na kojem se nalazi riječ dulje: {rečenica.find('dulje')} (find)")
print(f"Mjesto na kojem se nalazi riječ dulje: {rečenica.index('dulje')} (index)")

# razlika je u tome što vraćaju kad ne nađu ništa
if rečenica.find('kraće') == -1: # find() vraća -1 ako nije našao traženi string
    print("Kraće se ne nalazi u rečenici")
else:
    print("Kraće je u rečenici")

rečenica.index('kraće') # index() vraća ValueError ako ne nađe ništa

# %%
# dodatni argumenti za find ili index su raspon u kojem se traži
# pomicanjem ovog raspona može se naći sve instance nekog stringa, ne samo prvi
# koristimo casefold kako pretraga ne bi ovisila o malim i velikim slovima
pozicija1 = rečenica.casefold().find('malo', 0, 18) # od početka do 18 znaka
pozicija2 = rečenica.casefold().find('malo', 18) # od 18 do kraja

print(f"Prvo mjesto gdje se nalazi riječ malo: {pozicija1}\nDrugo mjesto gdje se nalazi riječ malo: {pozicija2}\n")

# obje metode imaju svoje varijante koje počinju od kraja, tj. s desne strane: rfind() i rindex()

print(f"Prvo pojavljivanje riječi dulje s lijeve strane: {rečenica.index('dulje')}")
print(f"Prvo pojavljivanje riječi dulje s desne strane: {rečenica.rindex('dulje')}")

# %%
# vrlo često pretražujemo string kako bi se izbrojalo broj puta koji se neki znak ili podstring pojavljuje
# za to služi metoda count()

primjer = "U ovoj rečenici ćemo brojati koliko puta se pojavljuju samoglasnici"

print(f"Koliko slova A ima u primjeru: {primjer.casefold().count('a')}")

primjer2 = "ababababab"
# ako postoji potencijalno preklapanje podstringova koji se traže onda se broje samo slučajevi bez preklapanja
print(f"Koliko puta za redom se pojavljuje string 'aba': {primjer2.count('aba')}")

# slično kao i find/index i count() može pretraživati samo u određenom rasponu, ne u cijelom stringu
# u primjeru ispod pretražujemo od polovice stringa (zaokruži se duljina/2) do kraja
broj = primjer.casefold().count('o',round(len(primjer)/2))
print(f"U zadnjoj polovici nalazi se {broj} slova 'O'.")

# %% [markdown]
# ### Provjera sadržaja stringa
# 
# Postoji više ugrađenih metoda koje služe za provjeru toga što se nalazi u stringu. Te metode obično počinju sa **is** i vraćaju *True* ili *False*

# %%
slova = "primjer"
brojke = "1234"
mix = "3m4j5ć6"
specijalni = "šč-df 01!"
print(f"Primjeri za koje se testira:\t{slova}\t{brojke}\t{mix}\t{specijalni}")
# isalnum() vraća True ako su znakovi slova ili brojke
print(f"Što isalnum() kaže za primjere:\t{slova.isalnum()}\t{brojke.isalnum()}\t{mix.isalnum()}\t{specijalni.isalnum()}")
# isaalpha() vraća True ako su znakovi slova
print(f"Što isalpha() kaže za primjere:\t{slova.isalpha()}\t{brojke.isalpha()}\t{mix.isalpha()}\t{specijalni.isalpha()}")
# isascii() vraća True ako su znakovi iz osnovne ASCII tablice
print(f"Što isascii() kaže za primjere:\t{slova.isascii()}\t{brojke.isascii()}\t{mix.isascii()}\t{specijalni.isascii()}")
# isdecimal() vraća true ako su znakovi decimalne znamenke 0-9
print(f"Što isdecimal kaže za primjere:\t{slova.isdecimal()}\t{brojke.isdecimal()}\t{mix.isdecimal()}\t{specijalni.isdecimal()}")
# isdigit() vraća true ako su znakovi brojčane znamenke
print(f"Što isdigit() kaže za primjere:\t{slova.isdigit()}\t{brojke.isdigit()}\t{mix.isdigit()}\t{specijalni.isdigit()}")
# isnumeric() vraća true ako je u stringu sadržane samo znamenke koje su brojevi
print(f"Što isnumeric kaže za primjere:\t{slova.isnumeric()}\t{brojke.isnumeric()}\t{mix.isnumeric()}\t{specijalni.isnumeric()}")
# isspace() vraća true ako su u stringu samo prazni znakovi
primjer = "\n     \t"
print(f"Jesu li u {primjer} samo prazni znakovi? {primjer.isspace()}")
#ovo je da malo vidimo razlike između metoda za provjeru brojeva
primjer="4\u00B2"
print(f"Sadrži li {primjer} samo znamenke:\t{primjer.isdigit()}\t{primjer.isnumeric()}\t{primjer.isdecimal()}")
primjer="-2.5"
print(f"Sadrži li {primjer} samo znamenke:\t{primjer.isdigit()}\t{primjer.isnumeric()}\t{primjer.isdecimal()}")


# %%
malo = "sve malo"
veliko = "SVE VELIKO"
mix = "Samo prvo"
naslov = "Sve Veliko"

print(f"Primjeri za koje se testira:\t{malo}\t{veliko}\t{mix}\t{naslov}")
# islower() provjerava je su li svi znakovi mali
print(f"Što islower() kaže za primjere:\t{malo.islower()}\t\t{veliko.islower()}\t\t{mix.islower()}\t\t{naslov.islower()}")
# isupper() provjerava jesu li svi znakovi veliki
print(f"Što isupper() kaže za primjere:\t{malo.isupper()}\t\t{veliko.isupper()}\t\t{mix.isupper()}\t\t{naslov.isupper()}")
# istitle() provjerava počinje li svaka riječ velikim slovom
print(f"Što istitle() kaže za primjere:\t{malo.istitle()}\t\t{veliko.istitle()}\t\t{mix.istitle()}\t\t{naslov.istitle()}")

#brojevi i specijalni znakovi ne utječu na rezultat ovih metoda
primjer = "ovdje ima i broj 1233!"
primjer.islower()

# %%
# isprintable() provjerava jesu li znakovi sadržani u stringu takvi da se mogu ispisati
primjer = "Ovo je rečenica."
print(f"Može li se {primjer} ispisati? {primjer.isprintable()}")
# makar se mogu slati na print() \t i \n iz nekog razloga ne spadaju u kategoriju printabilnog
# postoji još znakova koji ne služe za ispis na ekran, već za komunikaciju direktno između računala
primjer = "\t1.\t2.\t3."
print(f"Može li se {primjer} ispisati? {primjer.isprintable()}")

# isidentifier() provjerava je li string validno ime za varijablu u Pythonu
imena = ["varijabla12","neko ime","hešteg","#hešteg?"]
for primjer in imena:
    print(f"Može li {primjer} biti ime za varijablu? {primjer.isidentifier()}")

# %%
# startswith() i endswith() se koriste na identičan način
# kao što im ime govori provjeravaju počinje li (ili završava) naš string sa nekim specifičnim stringom

if "neki string".startswith("neki"):
    print("Ovaj string počinje sa 'neki'")
else:
    print("Ovaj string ne počinje sa 'neki'")

# može se provjeravati i više potencijalnih početaka/krajeva ako ih se zada u obliku ntorke
ime = "datoteka.txt"
if ime.endswith(('.csv','.txt')):
    print("Nastavak datoteke je jedan od tipičnih za tekstualne datoteke!")

# %% [markdown]
# ### Mijenjanje veličine slova
# 
# Ove metode mijenjaju znakove iz velikih u male i obratno (npr. a -> A)

# %%
malo = "ovo je string za primjer"
svakakvo = "ovO JE sTRing za PRIMJER"
# namješta string tako da izgleda kao normalna rečenica s prvim velikim slovom
malo.capitalize(), svakakvo.capitalize()

# %%
malo = "ovo je string za primjer"
svakakvo = "ovO JE sTRing za PRIMJER"
# namješta string tako da svaka riječ počinje velikim slovom (engleski naslovi)
malo.title(), svakakvo.title()

# %%
svakakvo = "ovO JE sTRing za PRIMJER ŠŠŠššš"

# upper() sva slova radi velika
veliko = svakakvo.upper()
print(f"Nakon upper(): {veliko}")

# lower() sva slova radi malenim
malo = veliko.lower()
print(f"Nakon lower(): {malo}")

# swapcase() radi zamjenu, ali je bilo veliko onda je malo i obratno
svakakvo.swapcase()


# %%
# casefold() se koristi kod uspredbi stringova kad ne želimo da veličina znaka utječe
malo = "šime"
veliko = "Šime"
print(f"Mala i velika slova nisu isto za python pa usporedba malo == veliko daje: {malo == veliko}")
if malo.casefold() == veliko.casefold():
    print("Ispiši ako se pojave ista slova, nevažno je li veliko ili malo")

# %% [markdown]
# ### Prilagodba stringa za ispis/učitavanje
# 
# Osim `format()` metode koja je glavna za prilagodbu poruka koji se stavljaju u print() ili write() postoji još metoda koje nam olakšavaju u pogledu gdje će se poruka i kako prikazivati.
# 
# format() i f-stringovi koji su zamjena za korištenje te metode, su predstavljene u ranijoj bilježnici (osnovni pregled stringova) tako da se ovdje neće ponovno raditi, ali su predstavljene ostale metode.

# %%
# center() ljust() i rjust() sve rade slično. osnovni argument koji ima dajemo je kolika je širina područja (broj znakova)
# one će ovisno o tom broju znakova dodati broj razmaka oko našeg stringa

# ovdje ćemo raditi sa širinom od 80 znakova
širina = 80
# center() dodaje razmake prije i poslije stringa kako bi bio u sredini
print("U sredini".center(širina))
# ljust() je skraćeno od left justified, dakle string će biti s lijeve strane, razmaci se dodaju desno
print("Lijevo".ljust(širina))
# rjust() je skraćeno od right justified, poruka se pomiče desno dodavanjem razmaka s lijeve strane
print("Desno".rjust(širina))

# %%
# ove metode dodaju razmak ako samo definiramo širinu, no mogu zapuniti bilo koji znak koji želimo
print("X".ljust(3,"O"))
print("X".center(3,"O"))
print("X".rjust(3,"O"))

# %%
# kao suprotnost ovim metodama radi različita verzija strip() metode
# strip() je zamišljen tako da miče prazna mjesta (ili druge znakove) koji su dodani za ispis

s = "sredina".center(60)
print(f"s je dugačak {len(s)} znakova i kad se ispiše izgleda kao:\n{s}")
# strip() miče prazne znakove i s lijeve i desne strane
print(f"Nakon strip() ostane {len(s.strip())} znakova:\n{s.strip()}")
# rstrip() ih miče samo s desne strane
print(f"Nakon rstrip() ostane {len(s.rstrip())} znaka:\n{s.rstrip()}")
# lstrip() ih miče samo s lijeve strane
print(f"ANakon lstrip() ostane {len(s.lstrip())} znaka:\n{s.lstrip()}")

#isto kao i za center, rjust i ljust možemo micati željeni znak, ne samo razmak
"OOOOOXXOO".strip("O")

# %%
široko = "\t".join(str(i) for i in range(5))
print(široko) # tab između svakog broja
# poruke u kojima postoji tab \t znak imaju neki standardni razmak
# s expandtabs() se \t mijenja za različiti broj razmaka (space)
print(široko.expandtabs(4)) # 4 razmaka između svakog broja
print(široko.expandtabs(20)) # 20 razmaka između svakog broja

# %% [markdown]
# ### Zamjena znakova unutar stringa
# 
# Sve ove metode služe za zamjenu znakova unutar stringa, ali računajte da kao i ostale metode za stringove zapravo rade novu kopiju stringa u kojoj postoje zamjene.

# %%
# osnovna metoda za zamjene je replace()
# ona traži podstring koji zadamo i mijenja ga za željeni novi sadržaj na svim mjestima gdje ga nađe

lista = "ime,prezime,broj telefona,adresa"
# replace() prima dva argumenta - traženi string i novi string s kojim se stari mijenja
novalista = lista.replace(',',' ') # mijenja sve , sa razmakom
print(f"Stara lista: {lista}")
print(f"Nova lista: {novalista}\n")

# ovo će prvo naći sve podstringove 'ime' i zamijeniti ih s 'Marko'
# nakon toga replace('prezime','Horvat') neće napraviti ništa jer 'prezime' više ne postoji
popuni1 = lista.replace('ime','Marko').replace('prezime','Horvat')
print(f"Lista s popunjenim imenom: {popuni1}")
# ovo prvo mijenja 'prezime' u Horvat
popuni2 = lista.replace('prezime','Horvat').replace('ime','Marko')
print(f"Lista s popunjenim imenom: {popuni2}")

# replace() prihvaća i dodatni argument koji govori na koliko mjesta treba zamijeniti podstrnig
# ako se ovo ne definira naprosto će ih zamijeniti sve
popuni3 = lista.replace('ime','Marko',1) # ovo će zamijeniti samo prvo 'ime' koje nađe
print(f"Lista s popunjenim imenom: {popuni3}")

# %%
# translate() se koristi za zamjenu jednih znakova drugima
# može mijenjati samo jedan znak za drugi kao replace()
# ali može napraviti i mnogo zamjena istovremeno (što mu je glavna namjena)

rečenica = "U ovoj rečenici ćemo zamijeniti sve samoglasnike sa nekim drugim samoglasnicima"

# translate() očekuje riječnik (dict) kao argument, a taj riječnik sadrži parove znakova za zamjenu
# ti parovi označavaju vrijednost znaka u unicode tablici
zamjene = {ord('a'):ord('e'), ord('e'):ord('i'), ord('i'):ord('o'), ord('o'):ord('u'), ord('u'):ord('a')}

print(f"Pogledajmo razlike:\nOriginal:\t{rečenica}\nSa zamjenama:\t{rečenica.translate(zamjene)}")

# %%
# na gornjem primjeru se vidi da ručna izrada riječnika za zamjenu izgleda nespretno
# zato postoji metoda koja služi specifično za izradu riječnika zamjene: maketrans()

zamjene2 = "".maketrans("aeiou","eioua") # ovo radi isti riječnik kao onaj iznad
if zamjene2 == zamjene:
    print("Ovo je isti riječnik zamjene :)")

# maketrans() u ovom primjeru uzima 2 argumenta
# originalni raspored znakova i novi raspored znakova
# znak na indeksu 0 u prvom stringu (originalni raspored) se onda mijenja sa znakom na indeksu 0 u drugom stringu

zamjene3 = "".maketrans("aeiou","eioua","čćšđž") # postoji i 3 opcionalni argument, to je lista znakova koji se miču iz originalnog

rečenica.translate(zamjene3)

# %% [markdown]
# ### Ostalo ...
# 
# U ovoj kategoriji ostale su metode koje ne spadaju ni u jednu od skupina namjena.

# %%
# ovdje je ostao samo encode()
# Python standardno koristi UTF-8 zapis za Unicode tablicu znakova
# pomoću ove metode možemo forsirati točno određeni zapis za znakove

"Ovo je rečenica sa 'našim' znakovima".encode(encoding="ascii",errors="replace")
# u ovom primjeru originalni string se zapisuje u ASCII encodingu
# drugi argument je način na koji se tretiraju znakovi koji nisu podržani u novom zapisu (u ovom primjeru mijenja ih se s ?)

# %% [markdown]
# ## Zbirka list

# %% [markdown]
# ### Dodavanje novih elemenata u listu
# 
# Ove metode služe za različite oblike dodavanja novih elemenata u postojeću listu.

# %%
lista = [1,2,3]

# .append() dodaje neki objekt na kraj liste kao novi element
lista.append(4)
lista.append("brojevi")
print(f"Ovako izgleda lista {lista} nakon što smo ju produljili")

# %%
# .extend() također dodaje elemente na kraj liste, ali kao argument uzima drugu zbirku ili iterator

listaA = [1,2,3]
listaB = [4,5,6]
# extend dodaje elemente druge liste jedan po jedan
listaA.extend(listaB)
print(f"Ovo je rezultat ako koristimo extend(): {listaA}")
# append bi cijelu listu dodao kao jedan član
listaA.append(listaB)
print(f"Ovo je rezultat ako koristimo append(): {listaA}")

# %%
# .insert() služi tome da se novi element doda na specifično mjesto
# svi ostali elementi u listi nakon toga se pomiču za jedno mjesto u desno (indeks im se promijeni za +1)

slova = ['A','B','C','D']
# na indeks 3 se dodaje novi element
slova.insert(3, 'Ć')
print(f"Popis slova: {slova}")
# element koji je prethodno bio na indeksu 3 se pomiče za +1, a isto rade i ostali elementi s većim indeksom
slova.insert(3, 'Č')
print(f"Popis slova: {slova}")

# %% [markdown]
# ### Micanje elemenata iz liste
# 
# Osim ključne riječi `del` koja se koristi za općeinto brisanje u Pythonu liste imaju i dodatne metode koje služe za uklanjanje elemenata iz liste.

# %%
popis = ['jaja','kruh','mlijeko','maslac','kruh']

# metoda .remove() nalazi element po njegovoj vrijednosti i miče prvi takav element ako ga nađe
popis.remove('kruh')
print(f"Popis nakon što se makne jedan element: {popis}")
# ako željene vrijednosti nema u listi onda javlja grešku!
popis.remove('jabuke')

# %%
popis = ['jaja','kruh','mlijeko','maslac']

# metoda .pop() miče element sa željenog indeksa, ali nam njegovu vrijednost vraća nazad kao rezultat
artikal = popis.pop(0) # miče element s indeksa 0
print(f"Popis sad izgleda ovako: {popis}")
print(f"Ako nam treba element iz liste smo spremili: {artikal}")

# česta namjena za korištenje pop() metode je preseljavanje elementa iz jedne liste u drugu
# npr. ako želimo listu stvari koje smo kupili, mičemo element iz originalne liste, ali stavljamo ga u popis kupljeno
kupljeno = [artikal]
kupljeno.append(popis.pop()) # ako pop() pozovemo bez indeksa on automatski uzima zadnji
print(f"Originalni popis je sad kraći: {popis}")
print(f"A popis kupljenih stvari je dulji: {kupljeno}")

# %%
popis = ['jaja','kruh','mlijeko','maslac']

# metoda .clear() naprosto briše sve elemente iz liste, ne uzima nikakav argument
popis.clear()
popis

# %% [markdown]
# ### Pretraživanje sadržaja liste
# 
# Ove metode nam služe za pronalaženje pozicije ili broja željenih elemenata.

# %%
abeceda = ['A','B','C','Č','Ć','D']

# metoda .index() radi identično kao i kod stringova, ako joj damo vrijednost elementa
# ona će nam vratiti prvi index na kojem se taj element nalazi
print(f"Pozicija slova C je {abeceda.index('C')}")

# za dodatne detalje on index() metodi pogledaj u odjeljak o stringovima jer rade identično

# %%
ocjene = [5,5,4,5,3,2,4,5,3,1,2,3,5,4,1,3,3,3]

# metoda .count() radi isto kao i kod stringova, vraća nam koliko puta se neki element pojavljuje u listi
# primjer: prebrojimo koliko ima kojih ocjena

brojOcjena = [ocjene.count(i) for i in range(1,6)]
print("Broj ocjena")
for ocjena,broj in enumerate(brojOcjena,start=1):
    print(f"{ocjena}: {broj}")

# %% [markdown]
# ### Sortiranje sadržaja liste
# 
# S obzirom da se elementi liste mogu preslagivati moguće ih je soritirati po različitim kriterijima.

# %%
imena = ['Ivan','Marko','Ana','Dominik','Petra','Đurđica']

# .sort() sortira elemente liste po zadanom ključu
imena.sort() # ako pozovemo sort() bez argumenata on sortira elemente liste uzlazno po vrijednosti
print(f"Popis imena sortiral uzlazno: {imena}")
# OPREZ: slovo Đ ima veću vrijednost od bilo kojeg znaka iz engleske abecede
# zato 'Đurđica' ne dolazi iza 'Dominik' kao što bi to bilo u hrvatskoj abecedi

brojevi = [33,105,21,4,-1]
brojevi.sort(reverse=True) # reverse je opcionalni argument koji se dodaje ako želimo sortirati silazno
print(f"Popis ovih brojeva silazno: {brojevi}")

# %%
# kompetna definicija metode sort omogućuje korištenje 2 opcionalna argumenta
# reverse je jedan od njih (prikazano iznad)
# drugi se zove key i služi za zadavanje funkcije koja je ključ za sortiranje

# primjer: sortirajmo popis imena po duljini imena, a ne po vrijednosti

def poDujini(riječ):
    return len(riječ) # sve što ova funkcija radi je vraća duljinu stringa kojeg dobije

imena.sort(key=poDujini) #VAŽNO: ovdje funkciju prosljeđujemo kao argument, pa ju navodimo bez zagrada!
print(f"Popis imena od najkraćeg prema najduljem: {imena}")

# %% [markdown]
# **Kako radi sortiranje po ključu**
# 
# `.sort()` uvijek sortira po vrijednosti, a argument `key` služi da zadamo novi način određivanja vrijednosti. *key* mora biti neka funkcija koja vraća željenu vrijednost. Dakle prije sortiranja moramo napraviti funkciju koja služi za izračun ključa (primjer iznad računa duljinu riječi). Kod sortiranja svi elementi liste se jedan po jedan prosljeđuju toj funkciji i zatim se sortiraju po vrijednosti koju ta funkcija vrati kao rezultat.

# %%
# još par primjera...

def poZadnjemSlovu(riječ):
    return riječ[-1] # vraćamo nazad zadnje slovo iz riječi

def poHrvatskojAbecedi(riječ):
    # počistimo riječ za lakše uspoređivanje
    riječ = riječ.strip().lower()
    # ideja je da vraćamo ispravan redoslijed u HR abecedi, tako da slijedi
    # HR abeceda bez dvostrukih znakova (dž, lj, nj)
    # prazna mjesta su ostavljena kako bi abeceda imala ispravnu duljinu
    abeceda = "abcčćd đefghijkl mn oprsštuvzž"

    # prva tri slučaja pokrivaju dvostruke znakove
    if riječ.startswith('dž'):
        return abeceda.find('d')+1
    elif riječ.startswith('lj'):
        return abeceda.find('l')+1
    elif riječ.startswith('nj'):
        return abeceda.find('n')+1
    # ovo je za slučaj da naiđemo na znak koji nije u hrvatskoj abecedi
    elif abeceda.find(riječ[0]) == -1:
        return len(abeceda)+ord(riječ[0])
    # za sva ostala slova se naprosto vraća njihova pozicija u abecedi
    else:
        return abeceda.find(riječ[0])

imena.sort(key=poZadnjemSlovu, reverse=True)
print(f"Popis imena poredan po zadnjem slovu imena, ali silazno: {imena}")

imena.extend(['William','Ljubica','Željka','Luka'])
print(f"\nRedoslijed prije sortiranja po HR abecedi: {imena}")
imena.sort(key=poHrvatskojAbecedi)
print(f"Popis sortiran ispravno po HR abecedi: {imena} ")

# %%
# ako samo želimo izokrenuti redoslijed liste onda koristimo metodu .reverse

imena.reverse()
print(f"Obrnuti redoslijed: {imena}")

# %% [markdown]
# ### Ostalo ...
# 
# Ostale metode definirane za liste koje ne spadaju niti u jednu od gornjih kategorija

# %%
prva = [1,2,3,4]
druga = prva
druga.append(5)
print(f"prva: {prva}\ndruga: {druga}\n")
# operator = ne kopira listu tako da druga.append(5) promijeni i prvu listu!

# .copy() metoda se koristi ako zapravo želimo novu kopiju liste
treća = prva.copy()
treća.append(6)
print(f"prva: {prva}\ndruga: {druga}\ntreća: {treća}")

# %% [markdown]
# ## Zbirka tuple

# %% [markdown]
# ### Pretraživanje sadržaja ntorke
# 
# S obzirom da su ntorke (eng. tuple) zapravo liste sa zamrznutim redoslijedom one imaju samo one metode koje rade s listama, ali koje ne mijenjaju redoslijed. Jedine dvije koje odgovaraju tom opisu su `index()` i `count()` koje rade identično kao i kod listi i stringova.

# %%
ocjene = (5,5,4,5,3,2,4,5,3,1,2,3,5,4,1,3,3,3)

# kako rade index() i count() je detaljnije objašnjeno u poglavlju o stringovima (način korištenja je identičan)

print(f"Prva pozicija ocjene 1: {ocjene.index(1)}") # index() vraća prvu poziciju na kojoj se nalazi vrijednost
print(f"Koliko ima jedinica: {ocjene.count(1)}") # count() broji koliko puta se vrijednost pojavljuje

# %% [markdown]
# ## Zbirka set

# %% [markdown]
# ### Operacije nad skupovima
# 
# Metode u ovoj skupini implementiraju operacije unije, presjeka i razlike, s time da za svaku od tih operacija postoji i specijalni operator:
# |Operacija|Oznaka operatora|Kombinacija na tipkovnici|
# |:-|:-:|:-|
# |Unija|&#124;|alt gr + W|
# |Presjek|&|shift+6|
# |Razlika|-|-|
# |Simetrična razlika|^|alt gr + 3 i nakon toga pritisni bilo što|

# %%
# skupovi koji sadrže znakove različitih abeceda
hr = set("abcčćdđefghijklmnoprsštuvzž")
en = {chr(vrijednost) for vrijednost in range(ord('a'),ord('z')+1)}
de = set("abcdefghijklmnopqrstuvwxyzäöüß")

# presjek
print(f"Znakovi zajednički hrvatskoj i engleskoj abecedi:\n{hr & en}") # pomoću operatora
print(f"Znakovi zajednički hrvatskoj i engleskoj abecedi:\n{hr.intersection(en)}") # pomoću metode intersection()

# .intersection() kao argument uzima drugi skup i vraća njihov presjek kao novi skup
# postoji i .intersection_update() verzija koja ne vraća novi skup nego mijenja sadržaj skupa nad kojim je pozvana metoda
# ovakva verzija postoji za sve operacije

de.intersection_update(en) # ovo će promijeniti sadržaj skupa de
print(f"DE više ne sadrži sve znakove od prije: {de}")

# %%
# razlika
# ovo funkcionira malo drugačije nego u matematici, postoje dvije verzije ovog operatora

# kod obične razlike redoslijed skupova je važan:
print(f"Znakovi koji nisu u engleskoj abecedi:\n{hr - en}")
print(f"Znakovi koji nisu u hrvatskoj abecedi:\n{en - hr}\n")

# isto to ali sa .difference() metodom:
print(f"Znakovi koji nisu u engleskoj abecedi:\n{hr.difference(en)}")
print(f"Znakovi koji nisu u hrvatskoj abecedi:\n{en.difference(hr)}\n")
# .difference_update() bi mijenjao sadržaj skupa nad kojim se poziva metoda

# kod simetrične razlike nije važan redoslijed 
print(f"Svi znakovi koji nisu zajednički za obje abecede:\n{hr ^ en}")
# ista stvar sa metodom
print(f"Svi znakovi koji nisu zajednički za obje abecede:\n{hr.symmetric_difference(en)}")

de = set("abcdefghijklmnopqrstuvwxyzäöüß")
de.symmetric_difference_update(en) # i ovdje postoji _update() verzija
print(f"Znakovi razlike između engleske i njemačke abecede: {de}")

# %%
# unija

zajedno = hr | en | de # naravno možemo raditi s više od jednog skupa
print(f"Zajednički skup svih znakova iz 3 abecede:\n{zajedno}")
# ista stvar se može napraviti s union() metodom
print(f"Zajednički skup svih znakova iz 3 abecede:\n{hr.union(en,de)}")

# za uniju ne postoji union_update() već se metoda samo zove update()
hr.update(en,de)
print(f"I dalje ćemo dobiti isti rezultat, ali sada smo izmjenili sadržaj skupa hr:\n{hr}")

# %% [markdown]
# ### Provjera odnosa skupova
# 
# Ove metode nam omogućuju provjeru odnosa između skupova (npr. podskup, nadskup i sl.). Sve počinju sa *is* i vraćaju True ako je uvjet zadovoljen.

# %%
prvi = {1,2,3,4,5,6,7}
drugi = {2,3,4}
treći = {6,7,8,9}

# issuperset() možemo koristiti za provjeru sadrži li u cijelosti jedan skup neki drugi skup
if prvi.issuperset(drugi):
    print("Prvi skup u sebi kompletno sadrži drugi skup")
else:
    print("Prvi skup u sebi ne sadrži kompletni drugi skup")

if prvi.issuperset(treći):
    print("Prvi skup u sebi kompletno sadrži treći skup")
else:
    print("Prvi skup u sebi ne sadrži kompletni treći skup")

# %%
# issubset() radi obrnuto, tj. provjerava je li naš skup podskup nekog drugog skupa
drugi.issubset(prvi)

# %%
# isdisjoint() se koristi za provjeru imaju li skupovi presjek
# ako presjek ne postoji vraća True kao rezultat
četvrti = {9,10,11}
prvi.isdisjoint(četvrti), prvi.isdisjoint(treći)

# %% [markdown]
# ### Dodavanje/micanje/kopiranje elemenata skupa
# 
# `union()` i `update()` se kao operacije mogu koristiti za dodavanje novih elemenata u skup, no postoji još metoda koje specifično služe za dodavanje i brisanje elemenata. Mnogo ovih metoda rade isto kao i za liste.

# %%
skup = {1,2,3,4}

# add() metoda dodaje novi element u skup
skup.add(5)
skup.add(3) # ako je element već u skupu neće se desiti ništa

skup

# %%
# brisanje elemenata iz skupa se može raditi na više načina

# discard() miče željeni element iz skupa
skup.discard(2)
skup.discard(6) # ako elemen nije u skupu neće se dogoditi ništa
print(f"Trenutni elementi skupa su: {skup}")

# remove() radi jednako kao i za liste
# ako element postoji miče ga iz skupa
skup.remove(1)
print(f"Trenutni elementi skupa su: {skup}")
# a ako ga nema javlja grešku
skup.remove(2)

# %%
# uz to dodane su i metode koje se koriste i kod listi
skup = {'a','b','c','d'}

# pop() radi slično kao i za liste, ali skupovi nemaju indeks
# tako da pop() naprosto izbaci neki element liste i vrati njegovu vrijednost kao rezultat
element = skup.pop() # ne prima argument
print(f"Izbačen je {element}")

# clear() radi identično kao i za liste, briše sadržaj cijelog skupa
skup.clear()
print(f"U skupu je ostalo: {skup}")

# %%
prvi = {'a','b','c','d'}
drugi = prvi
drugi.add('e')
# isto kao i za liste, korištenje = operatora neće napraviti kopiju, već samo novo ime za postojeći skup
print(f"Prvi: {prvi}\nDrugi: {drugi}\n")
# ako mijenjamo drugi promijenit će se i prvi

#tako da i skupovi imaju metodu copy() koja radi kopiju skupa ako to trebamo
treći = prvi.copy()
treći.add('f')
print(f"Prvi: {prvi}\nDrugi: {drugi}\nTreći: {treći}")

# %% [markdown]
# ## Zbirka dictionary

# %% [markdown]
# ### Metode za rječnike
# 
# Ovo dolazi kad krenemo raditi s rječnicima

# %%
rječnik = {'a':1, 'b':2}

for ključ,vrijednost in rječnik.items():
    print(f"Ključ:vrijednost -> {ključ}:{vrijednost}")


