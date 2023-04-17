# Documentation
## Introduction
Ce programme a pour but d'illustrer le fonctionnement de la Fourmi de Langton.

Dans sa conception initial, la Fourmi de Langton est un automate cellulaire inventé par Christopher Langton, contenant un jeu de règles simples :

* La fourmi peut se déplacer dans toutes les directions (haut, bas, gauche, droite)
* si la fourmi est sur une case blanche, elle tourne de 90° vers la droite, change la couleur de la case en noir, et avance d'une case
* si la fourmi est sur une case noire, elle tourne de 90° vers la gauche, change la couleur de la case en blanc, et avance d'une case
	
	On peut étendre ce jeux de règles en utilisant un système où les couleurs sont modifiées de manière cyclique, par exemple :
	
	Rouge &rarr; Bleu &rarr; Jaune &rarr; Vert &rarr; Rouge

On indique ensuite pour chaque couleur si la fourmi doit tourner à droite `"R"` ou à gauche `"G"`.
Les règles sont alors décrite simplement par une chaîne de caractères de la forme `"LRLRRLLR"` et l'on peut générer les couleurs aléatoirement pour chaque caractère de la chaîne.

La Fourmi de Langton classique est décrite alors par `"RL"`
Exemple de règles intéressantes :
* `"RL"` finit par faire une "autoroute" (motif périodique qui se répète à l'infini)
* `"RLR"` croît de manière chaotique
* `"RRLL"` croît de manière symétrique
* `"LRRRRRLLR"` remplit tout l'espace en dessinant un carré
* `"LLRRRLRLRLLR"` finit aussi par faire une "autoroute" mais  le motif est plus compliqué que 	celui de la fourmi de base
* `"RRLLLRLLLRRR"` dessine un triangle qui grandit et se déplace 

_Exemples tirés de wikipédia :_ https://en.wikipedia.org/wiki/Langton%27s_ant

## Page de démarrage

### Paramètres :
* **World size** : nombre de cases de la grille carrée
* **Base color** : couleur initiale de la grille, c'est aussi la première couleur utilisée pour les règles
* **X start position** : position en x de départ de la fourmi
* **Y start position** : position en y de départ de la fourmi
* **Direction** : orientation initiale de la fourmi. Les valeurs possibles sont `Up, Down, Left, Right`
* **Rule** : les règles utilisées par la fourmi, au format `RL`

### Boutons :
* **Launch** initialise la fourmi avec les paramètres donnés et passe dans la vue de simulation
* **Load** permet de charger une fourmi précédemment sauvegardée

## Vue de simulation 
* **Next** fait avancer la fourmi d'une itération
* **Previous** fait reculer la fourmi d'une itération
* **Play** fait avancer la fourmi automatiquement
* **Reverse** fait reculer la fourmi automatiquement jusqu'à ce qu'elle revienne à l'itération 0
* **Pause** met la simulation en pause
* **Reset** réinitialise la simulation
* **Speed** permet de régler l'intervalle de temps en millisecondes entre 2 itérations

## Barre de menu :
### File : 
* **New** permet revenir à l'écran de démarrage
* **Save** permet de sauvegarder la fourmi en cours
* **Load** permet de charger une fourmi précédemment sauvegardée (fichiers `.ant`)
* **Quit** ferme l'application

### Simulation
Contient les mêmes boutons que dans la vu de simulation

### Help
* **Document** affiche cet page
* **About** affiche des informations complémentaires sur le logiciel
