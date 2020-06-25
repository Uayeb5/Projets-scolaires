#coding-utf8

import time

print("Bienvenue dans le calculateur d'IMC")
time.sleep(1)
userName = input("Quel est votre nom ?\n> ")			
texte1 = "Bienvenue {} que voulez-vous faire ? "			
print(texte1.format(userName))

program_on = True

while program_on:
	choixMenu = input("> ")
	if choixMenu == "Bonjour":
		print("Bonjour, il me semble que l'on s'est déjà vus quelque part non ?")
		continue
	elif choixMenu == "IMC":
		taille = input("Quelle est votre taille ? Ex : 1.60 : ")
		taille = float(taille)

		poids = input ("Quel est votre poids ? Ex : 61.5 : ")
		poids = float(poids)

		calcul = poids / (taille * taille)
		print("Votre IMC est de :", calcul)
		if calcul < 16.5:
			print("Dénutrition")
			break
		elif calcul > 16.5 and calcul < 18.5:
			print("Maigreur")
			break
		elif calcul > 18.5 and calcul < 25:
			print("Corpulence normale")
			break
		elif calcul > 25 and calcul < 30:
			print("Surpoids")
			break
		elif calcul > 30 and calcul < 35:
			print("Obésité modérée")
			break
		elif calcul > 35 and calcul < 40:
			print("Obésité sevère")
			break
		elif calcul > 40:
			print("Obésité morbide")
			break

	elif choixMenu == "Quitter":
		break
	else:
		print("Commande introuvable, commandes disponibles : Bonjour / IMC / Quitter")
		continue

time.sleep(2)
print("Au revoir.")


