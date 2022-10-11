AEROPORTO (Città, Nazione, NumPiste)
VOLO (IdVolo, GiornoSett, CittàPart, OraPart, CittaArr, OraArr, TipoAereo)
AEREO (TipoAereo, NumPasseggeri, QtaMerci) 

1. Le città con un aereoporto di cui non è noto il numero di piste
SELECT Città
FROM AEROPORTO 
WHERE NumPiste is NULL (operatori per clausola where);

2. I tipi di aereo usati nei voli che partono da Torino
SELECT TipoAereo 
FROM VOLO 
WHERE CittàPart= 'Torino';

3. Le città da cui partono voli diretti a Bologna 
SELECT CittàPart 
FROM VOLO 
WHERE CittàArr= 'Bologna';

4.Le città da cui parte e arriva il volo con codice AZ274
SELECT CittàPart, CittàArr 
FROM VOLO 
WHERE IdVolo= ‘AZ274’

5.Il tipo di aereo, il giorno della settimana, l orario di partenza la cui città di partenza inzia 
per B e contiene O e l cui città di arrivo termina con A e contiene E 
SELECT TipoAereo, GiornoSett, Orapart
FROM VOLO 
WHERE CittàPart 'B%O%' 
WHERE CittàArr '%E%A';
