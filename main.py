# Type de paramétre
def majeur(age: int):
    if age <= 0:
        return False
    if age >= 18:
        return True
    return False

# Récuperer et afficher les infos d'une personne
def recuperer_info_personne(numero_personne):
   nom_personne = input("Nom de la personne " + str(numero_personne) + ":")
   age_personne = input("Age de la personne " + str(numero_personne) + ":")  
   return nom_personne, int(age_personne)

# Afficher les infos d'une personne
def afficher_info_personne(numero_personne, nom, age):
    print("La personne", numero_personne, "est", nom, "son âge est", age, "ans")
    print("Le nom posséde", len(nom), "caractères")
    if majeur(age):
        print("Il est majeur")
    else:
        print("Il est mineur")
# Récuperer et afficher les infos d'une personne
def recupere_afficher_personne(numero_personne):
    nom, age = recuperer_info_personne(numero_personne)
    afficher_info_personne(numero_personne, nom, age)

nb_personnes = 2
for i in range(nb_personnes):
    recupere_afficher_personne(i+1)
    