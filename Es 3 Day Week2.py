#Esercizio 3
Benz = float(input('Scrivi litri benzina serbatoio: '))
Eff = float(input('Scrivi efficienza carburante (Km/l):'))
Prezzo = float(input('Prezzo prezzo benzina (€/l) '))
dis = 100      #Km
costo = (dis/Eff)*Prezzo
km = Benz * Eff

print('Per 100 km percorsi il costo è di euro:', costo)
print('La distanza percorribile con il carburante disponibile è:', km)
