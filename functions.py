import re

students = [
    {"phone": "770123456", "nom": "Dupont", "prenom": "Jean", "classe": "1A", "note_devoir": 15.0, "note_projet": 16.5, "note_examen": 14.0, "moyenne": 15.17},
    {"phone": "780987654", "nom": "Martin", "prenom": "Claire", "classe": "2B", "note_devoir": 12.5, "note_projet": 14.0, "note_examen": 13.0, "moyenne": 13.17}
]

def validate_phone(phone):
    # Supprimer les espaces pour la validation
    phone = phone.replace(" ", "")
    
    # Vérifier que le numéro commence par 77, 78, 76, 70, ou 75 et contient exactement 9 chiffres
    pattern = r"^(77|78|76|70|75)\d{7}$"
    if not re.match(pattern, phone):
        return False
    
    # Vérifier l'unicité du numéro
    for student in students:
        if student["phone"].replace(" ", "") == phone:
            return False
    
    return True

def validate_note(note):
    try:
        note = float(note)
        return 0 <= note <= 20
    except ValueError:
        return False


def get_student_data():
    prenom = input("Entrez le prénom : ")
    nom = input("Entrez le nom : ")
    classe = input("Entrez la classe : ")

    while True:
        phone = input("Entrez le numéro de téléphone  : ")
        if validate_phone(phone):
            break
        print("Numéro de téléphone invalide ou déjà utilisé. Veuillez réessayer.")

    while True:
        note_devoir = input("Entrez la note du devoir (0-20) : ")
        if validate_note(note_devoir):
            note_devoir = float(note_devoir)
            break
        print("Note invalide. Veuillez réessayer.")

    while True:
        note_projet = input("Entrez la note du projet (0-20) : ")
        if validate_note(note_projet):
            note_projet = float(note_projet)
            break
        print("Note invalide. Veuillez réessayer.")

    while True:
        note_examen = input("Entrez la note de l'examen (0-20) : ")
        if validate_note(note_examen):
            note_examen = float(note_examen)
            break
        print("Note invalide. Veuillez réessayer.")

    moyenne = round((note_devoir + note_projet + note_examen) / 3, 2)

    student = {
        "prenom": prenom,
        "nom": nom,
        "classe": classe,
        "phone": phone,
        "note_devoir": note_devoir,
        "note_projet": note_projet,
        "note_examen": note_examen,
        "moyenne": moyenne
    }
    # print (student)
    students.append(student)

def display_students(students_list):
    if not students_list:
        print("Aucun étudiant n'est enregistré.")
        return

    print("{:<15} {:<15} {:<10} {:<15} {:<10} {:<10} {:<10} {:<15}".format(
         "Prénom", "Nom", "Classe", "Téléphone", "Devoir", "Projet", "Examen", "Moyenne"))
    print("-" * 100)
    for student in students_list:
        print("{:<15} {:<15} {:<10} {:<15} {:<10.2f} {:<10.2f} {:<10.2f} {:<15.2f}".format(
            student["prenom"], student["nom"], student["classe"], student["phone"],
            student["note_devoir"], student["note_projet"], student["note_examen"], student["moyenne"]
        ))

display_students(students)



# numero =input("Entrez un numero: ")
# if validate_note(numero):
#     print("Le numéro est valide")
# else:
#     print("Le numéro n'est pas valide")

