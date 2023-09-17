
![logo](exemple/logo.png)


# PROJET MULTIPLE SUBSTITUTION ENCRYPTION 2 (MSE 2)
-------------------------------------

Chiffrement par substitution multiple + obscurcissement

Programme de chiffrement de texte par substitution multiple en 3 étapes.

Pour but de recherche et jeu.

##**Description du Programme : Chiffrement par Substitution Multiple (MSE)**



##**Introduction**

Le programme de Chiffrement à Substitution Multiple (MSE) est conçu pour fournir un chiffrement de texte en utilisant 3 niveaux de substitution de caractères et de complexité. Développé depuis le 22 janvier 2019, le programme propose une approche unique du chiffrement de texte.


##**I. Initialisation**


##**BDC (Base de Données de Caractère)**
les fichiers all.txt, light_weight.txt et ultra_light_weight.txt contient les caractères qui vont être utilisés pour substituer les caractères.

Ces caractères sont ensuite divisé en deux groupes:
  - Le group A pour générer des clé de substituion.
  - Le groupe B pour ajouter des caractères, après la substituion.

Celui devient unique à chaque utilisateur, lorsqu'il chiffre pour la première fois un message.


- Le programme commence par importer des bibliothèques essentielles et les caractères du fichier BDC, comprenant les lettres minuscules et majuscules, les chiffres, la ponctuation et les caractères accentués.

- Les paramètres de configuration sont chargés depuis un fichier "setting.json", spécifiant l'ensemble de caractères à utiliser pour le chiffrement, l'inclusion de la ponctuation, des chiffres et des accents et d'autres paramètres.

- Elle va aussi inclure la longueur des groupes caractères qui font être choisis pour substituer, la longueur des caractères spéciaux (un groupe de caractère est choisi pour avoir une longueur plus petite), le nombre de clés et des facteurs de déplacement.



##**II. Générateur de Configuration Aléatoire**

- Le programme peut générer des paramètres (fichier setting.json) pseudo aléatoires. Les utilisateurs peuvent opter pour la création de configurations aléatoires.

- Avant d'être substitué, le programme applique plusieurs opérations sur le texte avant le chiffrement, le rendant complexe à déchiffrer.



##**III. Chiffrement**

- Le processus de chiffrement de base comprend 3 étapes :

  - Obscurcir le texte en le divisant en deux et en réarrangeant les caractères et appliquer des transformations supplémentaires et des améliorations de complexité.

  - Substituer les caractères en fonction des clés de chiffrement générées à partir de l'ensemble de caractères du fichier BDC.

  - Introduire des caractères dans une position choisit dans le texte de manière pseudo aléatoires du groupe B de caractères distinct.



##**IV. Génération de Bibliothèque de Clés**

- Le programme génère une bibliothèque de clés de substitution choisit à partir du groupe A.



##**V. Outils**

- Le fichier tools.py offre des outils essentiels tels que la génération d'une nouvelle BDC, la suppression des clés de chiffrement, le mélange des caractères du fichier BDC actuelle et le nettoyage, suppression des doublons du fichier du fichier BDC.


------------------------------------------------------------


##**Démo et mise en application**

exemple de message: hello fish
Etape 1:
hello fish --> hlfe hlsio
hlfe hlsio --> 鞆쟓𑃙笉悀⓰缴䓛Ћ쨬䢭䘚彀팑ⲭ኱ﳤﴻ윩𓃠鞆쟓𑃙笉悀⓰缴延단䱘渓왆繽돬搽엱ﻦ๥戃쑈ꯒ
鞆쟓𑃙笉悀⓰缴䓛Ћ쨬䢭䘚彀팑ⲭ኱ﳤﴻ윩𓃠鞆쟓𑃙笉悀⓰缴延단䱘渓왆繽돬搽엱ﻦ๥戃쑈ꯒ --> 


Etape 2:
ꯒ쑈戃๥ﻦ엱搽돬繽왆渓䱘단延缴⓰悀笉𑃙쟓鞆𓃠윩ﴻﳤ኱ⲭ팑彀䘚䢭쨬Ћ䓛缴⓰悀笉𑃙쟓鞆 ---> ꯒ쑈戃๥ﻦ엱搽돬繽왆渓䱘단延缴⓰悀笉𑃙쟓鞆𓃠윩ﴻﳤ኱ⲭ팑彀䘚䢭쨬Ћ䓛缴⓰悀笉𑃙쟓鞆


Etape 3:
쨴⼪񕽖ꯒ吒쑈뤎戃𐿿䊼桂꺘Ꮡ㷲𒏷๥穆䝄ﻦ楶֙𓉎俔엱眽좋𓇘폏鐡𝌠旧𐤩ꁹ񨺵寚搽䬕ਛ돬뤎繽왆ꪉｭ渓뒉𓍬䱘단𒇜㸺延䉨ᖘ㐰𒉄缴⓰⢆悀䑗
뿥笉峕𑃙힨ꇔ쟓큤𝛷낀ⵄ态ᬈ鞆娀ᘜ𓃠윩ﴻﳤ኱軣슎묎⾤ⲭ堹ℊ쇯揄㎧𒁛𒏆팑𓆺彀≉喈⯰焄崲紑䘚䢭鮣🤽鶏缿圴됡쨬궻➩Ћ𖠆🎠䓛缴鵙땙⓰犀悀칝堽       
𒉉။𓎆笉෇᎕ᒸ㘶壖煆𑃙쟓礨鞆


Cette vue d'ensemble offre une compréhension claire et détaillée de la fonctionnalité et du fonctionnement du programme MSE, la rendant accessible aux personnes non familières avec le projet.


![image du projet](exemple/captur_demo.PNG)



## Ressources
-------------------------------------------------------------------

Exemples de code secret: [codex.vu](https://bit.ly/theclawsofgod)

le monde merveilleux des secrets, des lettres et des chiffres !


0011211548862 - 33222 - 1452215482375L


