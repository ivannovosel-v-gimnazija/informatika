#Kriptografija v1.0
#ova datoteka sadrži definicije funkcija koje koristimo za
#šifriranje i kriptoanalizu

#šifrira jedan znak rotacijskom, tj. cezarovom šifrom
def rotirajZnak(znak,pomak):
    abeceda="ABCČĆDĐEFGHIJKLMNOPRSŠTUVZŽ"
    if znak in abeceda:
        rotirano = abeceda[(abeceda.index(znak)+pomak)%len(abeceda)]
    else:
        rotirano = znak
    return rotirano

# pronalazi modulo inverz broja a, ako je d duljina abecede
# ako postoji inverz funkcija će ga vratiti, ako ne onda će
# povratna vrijednost biti 0
def moduloInverz(a,d):
    for i in range(d):
        if (a*i)%d == 1:
            return i
    return 0

#šifrira jedan znak Afinom šifrom s faktorima a i b
#potrebno je prethodno provjeriti ima li faktor a svoj inverz
#jer ako nema onda će dešifriranje biti neizvedivo
def kriptirajZnakAfino(znak,a,b):
    abeceda="ABCČĆDĐEFGHIJKLMNOPRSŠTUVZŽ"
    if znak in abeceda:
        rotirano = abeceda[((abeceda.index(znak)*a)+b)%len(abeceda)]
    else:
        rotirano = znak
    return rotirano

#dešifrira jedan znak kriptiran Afinom šifrom s faktorima a i b
#ako je originalno kriptirano faktorima koji nemaju inverz
#dešifriranje neće uspjeti
def dekriptirajZnakAfino(znak,a,b):
    abeceda="ABCČĆDĐEFGHIJKLMNOPRSŠTUVZŽ"
    #ako inverz ne postoji dekriptirani tekst će biti samo A
    inverz = moduloInverz(a, len(abeceda))
    if znak in abeceda:
        rotirano = abeceda[inverz*(abeceda.index(znak)-b)%len(abeceda)]
    else:
        rotirano = znak
    return rotirano

#računa frekvencije pojavljivanja znakova u tekstu i vraća ih kao listu
#verzija kao na što smo radili na satu
def frekvencijeZnakova(tekst):
    abeceda="ABCČĆDĐEFGHIJKLMNOPRSŠTUVZŽ"
    brojZnakova=[0 for znak in abeceda]
    ukupnoZnakova=0
    for znak in tekst:
        if znak in abeceda:
            brojZnakova[abeceda.index(znak)] +=1
            ukupnoZnakova += 1
    frekvencije = [brojZnakova[i]/ukupnoZnakova for i in range(len(abeceda))]
    return frekvencije

#računa frekvencije pojavljivanja znakova u tekstu i vraća ih kao listu
#verzija malo drugačija od one na satu
#koristi metodu count() koja radi na stringovima
def frekvencijeZnakova2(tekst):
    abeceda="ABCČĆDĐEFGHIJKLMNOPRSŠTUVZŽ"
    brojZnakova=[]
    ukupnoZnakova=0
    for znak in abeceda:
        brojZnakova.append(tekst.count(znak))
        ukupnoZnakova += brojZnakova[abeceda.index(znak)]
    frekvencije = [brojZnakova[i]/ukupnoZnakova for i in range(len(abeceda))]
    return frekvencije

#pomakne prvu komponentu vektora tako da dođe na zadnje mjesto
#vektor je zapisan u obliku liste
def rotirajVektor(vektor):
    vektor.append(vektor.pop(0))
    return vektor

#računa skalarni produkt 2 jednako dugačka vektora
#vektori se prihvaćaju u obliku liste
def skalarniProdukt(vek1,vek2):
    produkt = 0
    for i in range(len(vek1)):
        produkt += vek1[i]*vek2[i]
    return produkt
