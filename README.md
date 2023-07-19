
![logo](exemple/logo.png)


![video demo](exemple/demo_video.gif)
# PROJET MSE 2
-------------------------------------

# MULTIPLE SUBSTITUTION ENCRYPTION
-------------------------------------

Chiffrement par substitution multiple + obscurcissement

Programme de chiffrement de texte par substitution multiple en 3 étapes.

Pour but de créer des messages codés avec des messages.

**Le programme est unique à son utilisateur, vous devez partager le code entier pour pouvoir communiquer avec d'autre personne.**


**Nom de version : CRC XVIII [ GOLIATH ]**

# Comment sa fonctionne ?

### INPUT --> A --> B --> C --> output
    
    
    **Initiation**
        Génération des clés de chiffrement
--------------------------------------------------------------------------
	
    **I) Bloc A**
        Une série de fonctions modifie le texte entré.
--------------------------------------------------------------------------
    **II) Bloc B**
        Une clé de chiffrement est choisie au hasard.
        Chaque caractère est substitué avec cette clé.
--------------------------------------------------------------------------
    **III) Bloc C**
    	[ Obscurcissement ]
        Ajoute des caractères dans le code après la substitution.


# Exemple
![Exemple](exemple/exemple.jpg)
En bleu, vous avez les caractères qui ont été substitués et en rouge les caractères qui ont été ajoutés **après** la substitution.

![Exemple](exemple/0.PNG)
![Exemple](exemple/1.PNG)
![Exemple](exemple/2.PNG)


# REQUIS
-------------------------------------
Pour copier le message automatiquement vous devez installer le module [pyperclip](https://pypi.org/project/pyperclip/)

	pip install pyperclip


# Attention
-----------------------------------
**Lorsque vous chiffrer votre premier message un fichier _keylib.keys_ va être généré, ce son vous clés de chiffrement gardez les à tous prix !**

# Usage
---------------------------
Usage :
	
	Mélanger les caractères spéciaux (avec le jeu de caractère actuel)
		mixer()

	Reconstruit le jeu de caractère actuel
		rebuild()

	Pour chiffrer plusieurs messages et le mettre dans un fichier :
		mse_cipher_file('result.txt',exemple_phrases_list)

	Pour déchiffrer plusieurs messages dans un fichier :
		mse_decipher_file('exemple.txt')

	Pour supprimer les clés de chiffrement :
		reinitialiser()

	Chiffrer un message :
		mse_cipher(message)

	Déchiffrer:
		mse_decipher(message)

	demo:
		demo()


# Conseille et Astuces
-------------------------------------------------------------------

> Vous pouvez chiffrer autre chose que des lettres (minuscules ou majuscules) comme les ponctuations, accents et chiffres pour celà écrivez 'true' devant les carctères que vous voulez chiffrer,(_setting_.json)

![setting file](exemple/example_setting.PNG)

> modifier, mélanger votre jeu de caractères

> modifier les paramètres du programme dans configs/setting.json

> optez plûtot pour un language de type "sms" du genre: tu fait quoi ---> tfk

> modifier la liste des ["caractères spéciaux"](https://github.com/flowlord/Multiple-Substitution-Encryption/blob/main/configs/init.py#L54)


-------------------------------------------------------------------

## Comment démarrer ?

	1) installer le module pyperclip avec l'aide de pip (pip install pyperclip)
	
	2) rendez-vous sur "main.py" puis lancez le programme
		La fonction "demo" pour donner un exemple de message chiffré
		En même temps vous aurez générer un fichier keylib.keys
		Ce sont vos clés de chiffrement gardez les à tous prix !

	3) Explorez, modifier vos paramètres (setting.json)
	
	4) Assurez-vous d'envoyer de manière sécurisée votre programme à une autre personne
		Je dis bien tout le code source et pas seulement vos clés

![image du projet](exemple/captur_demo.PNG)



## Ressources
-------------------------------------------------------------------

Exemples de code secret : [codex.vu](https://bit.ly/theclawsofgod)

le monde merveilleux des secrets, des lettres et des chiffres !

twitter: [https://twitter.com/motionkerling](https://twitter.com/loofy_off)

0011211548862 - 33222 - 1452215482375L
