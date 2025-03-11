class Dictionary:

    #questa classe deve gestire il dizionario di una singola lignua, dovrà leggere il file
    #da esso raccogliere le info in una lista locale, oltre che dare modo alle altre classi
    #di consultare il dizionario
    def __init__(self):
        self._dict = None
        self.dictionary = []


    def loadDictionary(self,path):
        with open(path, "r") as file:
            list = []
            for line in file:
                if(line.strip().isalpha()):
                    self.replaceChars(str(line))
                    list.append(line.lower())
            dictionary = list.copy()


    def printAll(self):
        res = ""
        for s in self.dictionary:
            res += str(s)
        print(res)

    def replaceChars(self, text):
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text

    @property
    def dict(self):
        _dict = self.dictionary.copy()
        return self._dict