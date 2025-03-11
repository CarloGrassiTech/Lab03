import dictionary
import richWord
d = dictionary.Dictionary()

class MultiDictionary:

    def __init__(self):
        self.engDict = []
        self.itaDict = []
        self.spaDict = []

    def printDic(self, language):
        if language.lower == "english":
            self.engDict = d.dictionary.copy()
            for s in self.engDict:
                print(f"{s}")
        elif language.lower == "italian":
            self.itaDict = d.dictionary.copy()
            for s in self.itaDict:
                print(f"{s}")
        elif language.lower == "spanish":
            self.spaDict = d.dictionary.copy()
            for s in self.spaDict:
                print(f"{s}")


    def searchWord(self, words, language):
        """
        cercare una specifica parola nel dizionario della lingua selezionata e
        restituisce una lista di RichWord, con indicazione se
        la parola è stata trovata nel dizionario (e quindi è corretta) oppure no
        :value words: consiste
        :value language:
        :exception :
        """
        countError = 0
        wrongWords=[]
        if language.lower() == "english":
            for w in words.split():
                self.engDict = d.dictionary.copy()
                rw = richWord.RichWord(w)
                if not self.engDict.__contains__(w):
                    countError +=1
                    wrongWords.append(w)
                    rw.corretta(w, False)
                else:
                    rw.corretta(w, True)
        elif language.lower() == "italian":
            for w in words.split():
                self.itaDict = d.dictionary.copy()
                if not self.itaDict.__contains__(w):
                    countError += 1
                    wrongWords.append(w)

        elif language.lower() == "spanish":
            for w in words.split():
                self.spaDict = d.dictionary.copy()
                if not self.spaDict.__contains__(w):
                    countError += 1
                    wrongWords.append(w)
        print("--------------------------------------------------")
        print("Using __contains__")
        for l in wrongWords:
            print(f"{l}")



