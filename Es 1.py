# Esercizio 1
str_input = input('Scrivi una frase: ')
Nuovo = ''
i = 0
while i < len(str_input):
    if str_input[i] != 'a' and str_input[i] != 'e' and str_input[i] != 'i'and str_input[i] != 'o' and str_input[i] != 'u': # se input di indice i diverso da vocale lo trasforma in maiuscolo
        vecchio = str_input[i]
        nuovo = nuovo + vecchio. superiore()
    else:                                                                                                                        #altrimenti ricopio il carattere di indice i così com'è
        nuovo = nuovo+str_input[i]
    i = i + 1
stampa(nuovo)