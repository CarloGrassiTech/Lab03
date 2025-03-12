import datetime
import time
import dictionary
import multiDictionary

class SpellChecker:
    #fa da interfaccia fra l'utente e la classe MultiDictionary
    def __init__(self):
        self.md=multiDictionary.MultiDictionary()

    def handleSentence(self, txtIn, language):
        self.md.searchWord(txtIn, language)





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
        chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
        for c in chars:
            text = text.replace(c, "")
        return text