from sys import stdin
import timeit
tstart = timeit.default_timer()


class Kubbe:
    vekt = None
    neste = None
    def __init__(self, vekt):
        self.vekt = vekt
        self.neste = None

def spor(kubbe):
    # SKRIV DIN KODE HER
    # kubbe = forste
    tempHoyest = kubbe.vekt

    while True:
        kubbe = kubbe.neste
        if kubbe.vekt > tempHoyest:
            tempHoyest = kubbe.vekt
        if kubbe.neste == None:
            break
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
tend = timeit.default_timer()
print('time: {}'.format(tend - tstart))
