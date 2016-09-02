from sys import stdin

class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None

def spor(kubbe):
    # SKRIV DIN KODE HER
    tempHoyest = kubbe.vekt
    
    while kubbe != None:
        if kubbe.vekt > tempHoyest:
            tempHoyest = kubbe.vekt
        kubbe = kubbe.neste
    return(tempHoyest)

# Oppretter lenket liste
forste = None
siste = None
for linje in stdin:
    forrige_siste = siste
    siste = Kubbe(int(linje))
    if forste == None:
        forste = siste
    else:
        forrige_siste.neste = siste

# Kaller loesningsfunksjonen og skriver ut resultatet
print(spor(forste))
