#coding:utf-8
import time

print("Bonjour \n")

time.sleep(1)

userName = input("Quel est votre nom ? \n")			
texte1 = "Bienvenue {} \n"					
print(texte1.format(userName))

time.sleep(1)

prixHT = input("Entrez un prix HT : \n")			
prixHT = int(prixHT)						
prixTTC = prixHT + (prixHT * 20 / 100)
print("Prix TTC : {}".format(prixTTC))
