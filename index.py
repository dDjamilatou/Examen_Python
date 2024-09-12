from functions import *

def menu():
    while True:
        print("\nMenu Principal")
        print("1. Afficher tout")
        print("2. Trier et afficher (par ordre décroissant de la moyenne)")
        print("3. Rechercher selon un critère")
        print("4. Modifier les notes d'un étudiant")
        print("5. Sortir")

        choice = input("Choisissez une option : ")

        if choice == '1':
            display_students(students)
        elif choice == '2':
            sort_and_display()
        elif choice == '3':
            criteria = input("Rechercher par (phone, nom, prenom, classe) : ")
            value = input(f"Entrez la valeur pour {criteria} : ")
            search_student(criteria, value)
        elif choice == '4':
            phone = input("Entrez le numéro de téléphone de l'étudiant à modifier : ")
            modify_student_notes(phone)
        elif choice == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    while True:
        get_student_data()
        continue_input = input("Voulez-vous continuer à ajouter des étudiants ? (o/n) : ").lower()
        if continue_input != 'o':
            break
    menu()
# menu