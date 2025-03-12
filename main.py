
import spellchecker
sc = spellchecker.SpellChecker()
while(True):
    d = {}
    flag = True
    ans = 0
    while flag:
        try:
            sc.printMenu()
            numb = int(input())
            if numb == 4:
                exit()
            if numb == 1 or numb == 2 or numb ==3:
                flag = False
                ans = int(numb)
            else:
                print("inserire un numero valido tra 1 e 3")
        except ValueError:
            print("inserire un valore tra 1 e 3")
    # Add input control here!

    if int(ans) == 1:
        print("Inserisci la tua frase in Italiano\n")
        txtIn = input()
        sc.handleSentence(txtIn,"italian")
        continue

    if int(ans) == 2:
        print("Inserisci la tua frase in Inglese\n")
        txtIn = input()
        sc.handleSentence(txtIn,"english")
        continue

    if int(ans) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        txtIn = input()
        sc.handleSentence(txtIn,"spanish")
        continue

    if int(ans) == 4:
        break


