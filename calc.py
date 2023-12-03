def calculer_moyenne(nombre, *args):
    if nombre <= 0:
        raise ValueError("Le nombre d'éléments doit être supérieur à zéro.")
    
    if len(args) != nombre:
        raise ValueError(f"Le nombre d'éléments fourni ({len(args)}) ne correspond pas au nombre spécifié ({nombre}).")
    
    somme = sum(args)
    moyenne = somme / nombre
    return moyenne

# Exemple d'utilisation :
try:
    nombre_elements = int(input("Entrez le nombre d'éléments : "))
    elements = [float(input(f"Entrez l'élément {i + 1} : ")) for i in range(nombre_elements)]
    
    resultat = calculer_moyenne(nombre_elements, *elements)
    print(f"La moyenne des éléments est : {resultat}")

except ValueError as e:
    print(f"Erreur : {e}")
except Exception as e:
    print(f"Une erreur inattendue s'est produite : {e}")