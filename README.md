# Projet-IN200 :

## Groupe de TD : S2LDDMPTD01

## Membres :

- Lucia
- Fernanda
- Mariama
- Nathan

## Objectif :

Implémenter la Fourmi de Langton en python et avoir une interface graphique permettant de visualiser le comportement de
cet automate.

## Organisation :

- **Simulation** : Lucia, Fernanda
- **GUI** : Mariama, Nathan

- **Responsable Github** : Nathan
- **Responsable de la qualité du code** : Lucia et Fernanda


# Installation :



**Attention :** l'utilisation d'un environnement conda est très fortement déconseillée car conda ne supporte pas les fonts truetype et ne permet pas à Tkinter de les utiliser. Pour une meilleure expérience il est donc conseillé d'utiliser virtualenv:

- **linux :**
pour créer l'environnement :
`python3 -m venv "env"`
`source ./env/bin/activate`
`pip3 install -r requirements.txt`
et pour lancer l'application : 
`python3 main.py`
ou plus simplement : 
`./setup.sh`
`./launch.sh`

- **windows :**
pour créer l'environnement :
 `python3 -m venv "env"`
 `.\venv\Scripts\activate`
 `pip3 install -r requirements.txt`
 et pour lancer l'application : 
 `python3 main.py`
 
 *note : il est recommandé d'utiliser python3.11, mais cela devrait marcher pour les versions >= 3.9*
