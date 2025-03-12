import richWord
import spellchecker

class Dictionary:

    #questa classe deve gestire il dizionario di una singola lignua, dovrà leggere il file
    #da esso raccogliere le info in una lista locale, oltre che dare modo alle altre classi
    #di consultare il dizionario
    def __init__(self):
        self._dict = None
        self.dictionary = []
        #lista di tuple parola e valore booleno True se la parola è corretta e
        #e valore False se la parola è errata


    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as file:
            list = []
            for line in file:
                spellchecker.SpellChecker.replaceChars(str(line))
                temp = line.strip()
                if(temp.isalpha()):
                    list.append(temp)
            self.dictionary = list
            return self.dictionary


    def printAll(self):
        res = ""
        for s in self.dictionary:
            res += str(s[0])
            res += "\n"
        print(res)


    @property
    def dict(self):
        _dict = self.dictionary.copy()
        return self._dict