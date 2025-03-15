import datetime
import dictionary
import richWord
class MultiDictionary:
#questa classe deve gestire il dizionario di una singola lingua, dovrà leggere
#il file e raccogliere le informazioni in una lista locale, oltre che a dare
#modo alle classi di consultare il dizionario
    def __init__(self):
        d = dictionary.Dictionary()
        self.engDict = d.loadDictionary("resources/English.txt")
        self.itaDict = d.loadDictionary("resources/Italian.txt")
        self.spaDict = d.loadDictionary("resources/Spanish.txt")


    def printDic(self, language):
        if language.lower == "english":
            for s in self.engDict:
                print(f"{s}")
        elif language.lower == "italian":
            for s in self.itaDict:
                print(f"{s}")
        elif language.lower == "spanish":
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

        tic = datetime.datetime.now()
        wrongWords = []
        if language.lower() == "english":
            for w in words.split():
                if not w in self.engDict:
                    wrongWords.append(w)

        elif language.lower() == "italian":
            for w in words.split():
                if not w in self.itaDict:
                    wrongWords.append(w)

        elif language.lower() == "spanish":
            for w in words.split():
                if not w in self.spaDict:
                    wrongWords.append(w)

        print("--------------------------------------------------")
        print("Using __contains__")
        for l in wrongWords:
            print(f"{l}")
        toc = datetime.datetime.now()
        print(f"Tempo di esecuzione: {toc - tic} secondi")
        print("--------------------------------------------------")

    def searchWordLinear(self, words, language):
        """
        Iterare su tutti gli elementi del vocabolario a partire dal primo. La ricerca termina quando viene trovato
        l’elemento cercato o si raggiunge l’ultimo, nel caso in cui l’elemento cercato non sia presente nella lista.
        :param words:
        :param language:
        :return:
        """
        tic = datetime.datetime.now()
        wrongWords = []
        if language.lower() == "english":
            for w in words.split():
                flag = True
                for line in self.engDict:
                    if line == w:
                        flag = False
                        break
                if flag:
                    wrongWords.append(w)

        elif language.lower() == "italian":
            for w in words.split():
                flag = True
                for line in self.itaDict:
                    if line == w:
                        flag = False
                        break
                if flag:
                    wrongWords.append(w)

        elif language.lower() == "spanish":
            for w in words.split():
                flag = True
                for line in self.spaDict:
                    if line == w:
                        flag = False
                        break
                if flag:
                    wrongWords.append(w)

        print("--------------------------------------------------")
        print("Using linear search")
        for l in wrongWords:
            print(f"{l}")
        toc = datetime.datetime.now()
        print(f"Tempo di esecuzione: {toc - tic} secondi")

    def searchWordDichotomic(self, words, language):
        #devo numerare il dizionario
        tic = datetime.datetime.now()
        wrongWords = []
        if language.lower() == "english":
            for w in words.split():
                confrontoParola = ""
                flag = True
                tempDiz = self.engDict.copy()
                while flag:
                    conforntoParola = tempDiz[int(len(tempDiz) / 2)]
                    if w == confrontoParola:
                        flag = False
                        wrongWords.append(w)
                    elif w < confrontoParola: #se True cerco nella meta superiore
                        tempDiz = tempDiz[0:int(len(tempDiz)/2)]
                    else: #se sono qui devo cercare nella metà inferiore
                        tempDiz = tempDiz[int(len(tempDiz)/2):len(tempDiz)]
                    if len(tempDiz) == 1 and flag:
                        wrongWords.append(w)
                        break



        elif language.lower() == "italian":
            for w in words.split():
                confrontoParola = ""
                flag = True
                tempDiz = self.itaDict.copy()
                while flag:
                    conforntoParola = tempDiz[int(len(tempDiz) / 2)]
                    if w == confrontoParola:
                        flag = False
                        wrongWords.append(w)
                    elif w < confrontoParola:  # se True cerco nella meta superiore
                        tempDiz = tempDiz[0:int(len(tempDiz) / 2)]
                    else:  # se sono qui devo cercare nella metà inferiore
                        tempDiz = tempDiz[int(len(tempDiz) / 2):len(tempDiz)]
                    if len(tempDiz) == 1 and flag:
                        wrongWords.append(w)
                        break

        elif language.lower() == "spanish":
            for w in words.split():
                wrongWords = []
                confrontoParola = ""
                flag = True
                tempDiz = self.spaDict.copy()
                while flag:
                    conforntoParola = tempDiz[int(len(tempDiz) / 2)] #int() prende solo la parte intera troncando la parte decimale
                    if w == confrontoParola:
                        flag = False
                        wrongWords.append(w)
                    elif w < confrontoParola:  # se True cerco nella meta superiore
                        tempDiz = tempDiz[0:int(len(tempDiz) / 2)]
                    else:  # se sono qui devo cercare nella metà inferiore
                        tempDiz = tempDiz[int(len(tempDiz) / 2):len(tempDiz)]
                    if len(tempDiz) == 1 and flag:
                        wrongWords.append(w)
                        break

        print("--------------------------------------------------")
        print("Using dicotomic search")
        for l in wrongWords:
            print(f"{l}")
        toc = datetime.datetime.now()
        print(f"Tempo di esecuzione: {toc - tic} secondi")

