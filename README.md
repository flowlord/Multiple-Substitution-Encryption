<p align="center">
  <img src="exemple/logo.png" />
</p>

<div align="center">

  # PROJET MULTIPLE SUBSTITUTION ENCRYPTION (MSE)
  -------------------------------------

  Logiciel de chiffrement par multiple substitution avec obscurcissement, pour la création de jeux d'énigme et de recherche.
  
  Chiffrement de texte par multiple substitution en 3 étapes.

  Nom de version: MSE-V27003 [ Complex Urulu ]
  
  Auteur: Enron Group
  
  version: 27.0.3
  
  date: 29 décembre 2023
  

</div>


## Mise à jour
    MSE-V27003

      - Bug inconnu à fait que nous avons écrasé cette version par une ancienne version (MSE-V27.0-Complex-Urulu)

      - Correction du bug dans configs_setting.py le try remplacé par os.path.exists


<br>

## Introduction
-------------------------------------
  Le programme de Chiffrement à Substitution Multiple (MSE) est conçu pour fournir un chiffrement de texte en utilisant trois niveaux de substitution de caractères et de complexité. Développé depuis le 22 janvier 2019, le programme propose une approche unique du chiffrement de texte.


## I. Initialisation
-------------------------------------

  ### BDC (Base de Données de Caractère)
  Les fichiers `all.txt`, `light_weight.txt` et `ultra_light_weight.txt` contient les caractères qui vont être utilisés pour substituer les caractères.


  Ces caractères sont ensuite divisés en deux groupes :

    - Le groupe A pour générer de la clé de substitution.

    - Le groupe B pour ajouter des caractères, après la substitution.


  Celui devient unique à chaque utilisateur, lorsqu'il chiffre pour la première fois un message.


  - Le programme commence par importer des bibliothèques essentielles et les caractères du fichier BDC, comprenant les lettres minuscules et majuscules, les chiffres, la ponctuation et les caractères accentués.


  - Les paramètres de configuration sont chargés depuis un fichier `setting.json`, spécifiant l'ensemble de caractères à utiliser pour le chiffrement, l'inclusion de la ponctuation, des chiffres et des accents et d'autres paramètres.


  - Elle va aussi inclure la longueur des groupes caractères qui font être choisis pour substituer, la longueur des caractères spéciaux (un groupe de caractère est choisi pour avoir une longueur plus petite), le nombre de clés et des facteurs de déplacement.

<br>

## II. Générateur de paramètre pseudo aléatoire
-------------------------------------
  - Le programme peut générer des paramètres (fichier `setting.json`) pseudo aléatoires. Les utilisateurs peuvent opter pour la création de configurations pseudo aléatoires.

  - Avant d'être substitué, le programme applique plusieurs opérations sur le texte avant le chiffrement, le rendant complexe à déchiffrer.


<br>


## III. Chiffrement
-------------------------------------
  - Le processus de chiffrement de base comprend 3 étapes :

    - Obscurcir le texte en le divisant en deux et en réarrangeant les caractères et appliquer des transformations supplémentaires et des améliorations de complexité.

    - Substituer les caractères en fonction des clés de chiffrement générées à partir de l'ensemble de caractères du fichier BDC.

    - Introduire des caractères dans une position choisit dans le texte de manière pseudo aléatoires du groupe B de caractères distinct.

<br>

## IV. Génération d'une bibliothèque de clés
-------------------------------------
  - Le programme génère une bibliothèque de clés de substitution choisit à partir du groupe A.

<br>

## V. Outils
-------------------------------------
  - Le fichier `tools.py` offre des outils essentiels tels que la génération d'une nouvelle BDC, la suppression des clés de chiffrement, le mélange des caractères du fichier BDC actuelle et le nettoyage, suppression des doublons du fichier du fichier BDC.

<br>

## Démo et mise en application
-------------------------------------

![Exemple d'utilisation](exemple/captur_demo.PNG)

  Testez le google colab maintenant pour un petit aperçu: [ici](https://colab.research.google.com/drive/1WWT81_UlmaZ9kKG6FbfdQ-ac4muXzYBf?usp=sharing)

<br>


`Ceci est que la base du code, regardez le code d'un autre point de vue et vous pouvez voire des miiliards de possibilité !`

<div align="center">
  le monde merveilleux des secrets, des lettres et des chiffres !
</div>



