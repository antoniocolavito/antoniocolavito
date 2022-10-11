 /* 
DISCO(NroSerie, TitoloAlbum,Anno,Prezzo) 
CONTIENE(NroSerieDisco,CodiceReg,NroProg) 
ESECUZIONE(CodiceReg,TitoloCanz,Anno) 
AUTORE(Nome,TitoloCanzone) 
CANTANTE(NomeCantante,CodiceReg) 
*/

1. 
-- 	I cantautori (persone che hanno cantato e scritto la stessa canzone) il cui nome inizia per 'D' --
SELECT NomeCantante 
FROM CANTANTE JOIN ESECUZIONE ON                              # La tabella di sx che prendiamo, ossia CANTANTE
CANTANTE.CodiceReg=ESECUZIONE.CodiceReg                       #equivalenza
JOIN AUTORE ON ESECUZIONE.TitoloCanz=AUTORE.TitoloCanzone     #unisco attributi con nomi diversi 
WHERE Nome=NomeCantante AND Nome LIKE 'D%';                   #Inserisco la condizione con l'operatore clausola AND (congiunzione) e LIKE (del tipo) 

2.
-- I titoli dei dischi che contengono canzoni di cui non si conosce l'anno di registrazione --
SELECT TitoloAlbum 
FROM DISCO.NroSerie INNER JOIN CONTIENE ON DISCO.NroSerie=CONTIENE.N       #in On vanno solo che condizioni di join
JOIN ESECUZIONE ON CONTIENE.CodiceReg = ESECUZIONE.CodiceReg
WHERE ESECUZIONE.Anno is NULL ; 

3.
-- I cantanti che non hanno mai registrato una canzone come solisti --
SELECT DISTINCT NomeCantante #utilizzo l'istruzione per ottenere valoti distinti 
FROM CANTANTE 
WHERE NomeCantante NOT IN #negazione e appartenenza (operatori WHERE) #group by? RAGGRUPPAMENTO
( SELECT S1.NomeCantante #Query interna
  FROM CANTANTE AS S1 
  WHERE CodiceReg NOT IN  #condizioni di confronto ANY o ALL? 	
  ( SELECT CodiceReg 
	FROM CANTANTE S2 
    WHERE S2.NomeCantante <> S1.NomeCantante ) ); #diverso
 
4.
-- I cantanti che hanno sempre registrato canzoni come solisti --
SELECT DISTINCT NomeCantante 
FROM CANTANTE 
WHERE NomeCantante NOT IN 
( SELECT C1.NomeCantante 
 FROM CANTANTE AS C1 JOIN ESECUZIONE ON CodiceReg=C1.CodiceReg 
 JOIN CANTANTE AS C2 ON CodiceReg=C2.CodiceReg ) 
 WHERE C1.NomeCantante <> C2.NomeCantante);

				
