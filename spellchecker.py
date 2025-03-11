import time

import dictionary
import multiDictionary
md = multiDictionary.MultiDictionary()
d = dictionary.Dictionary()
class SpellChecker:
    #fa da interfaccia fra l'utente e la classe MultiDictionary
    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):
        start_time = time.time()
        if language.lower()=="italian":
            d.loadDictionary("resources/Italian.txt")
            md.searchWord(txtIn, language)
        if language.lower() == "english":
            d.loadDictionary("resources/English.txt")
            md.searchWord(txtIn, language)
        if language.lower() == "spanish":
            d.loadDictionary("resources/Spanish.txt")
            md.searchWord(txtIn, language)
        end_time = time.time()
        print(f"Tempo di esecuzione: {end_time - start_time:.6f} secondi")



    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    pass