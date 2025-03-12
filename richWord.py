import dictionary

class RichWord:
#questa classe ha come ogni istanza al suo interno una parola del testo in input,
#l'indicazione di tale parola se risulti corretta o meno tramite un boolean
#posso usare questa classe per filtrare le parole corrette durente l'esercizio
    def __init__(self, parola):
        self._parola = parola # this is a string
        self._corretta = None #this is a bool

    @property
    def corretta(self):
        # print("getter of parola called" )
        return self._corretta

    @corretta.setter
    def corretta(self, boolValue):
        # print("setter of parola called" )
        self._corretta = boolValue

    def __str__(self):
        return self._parola