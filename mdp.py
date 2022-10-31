import random

minuscule = "abcdefghijklmnopqrstuvwxyz"
majuscule = "ABCDEFGHIJKMNOPQRSTUVWXTYZ"
nombre = "0123456789"
symboles = "/]}@\?[#%&"

generer = minuscule + majuscule + nombre + symboles
longueur_mdp = 10
MotDePasse = "".join(random.sample(generer, longueur_mdp))

print("Ton MDP généré est: " + MotDePasse)