class Vehicule:
    def __init__(self, marque, modele, couleur, vitesse_max):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.vitesse_max = vitesse_max

    def afficher_details(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Couleur: {self.couleur}, Vitesse max: {self.vitesse_max} km/h")

    def freiner(self):
        print(f"{self.marque} {self.modele} est en train de freiner.")

class Thermique(Vehicule):
    def __init__(self, marque, modele, couleur, vitesse_max, capacite_reservoir):
        super().__init__(marque, modele, couleur, vitesse_max)
        self.capacite_reservoir = capacite_reservoir

    def afficher_details(self):
        super().afficher_details()
        print(f"Capacité du réservoir: {self.capacite_reservoir} litres")

class Electrique(Vehicule):
    def __init__(self, marque, modele, couleur, vitesse_max, capacite_batterie):
        super().__init__(marque, modele, couleur, vitesse_max)
        self.capacite_batterie = capacite_batterie

    def afficher_details(self):
        super().afficher_details()
        print(f"Capacité de la batterie: {self.capacite_batterie} kWh")

class VoitureThermique(Thermique):
    def __init__(self, marque, modele, couleur, vitesse_max, capacite_reservoir, nombre_portes):
        super().__init__(marque, modele, couleur, vitesse_max, capacite_reservoir)
        self.nombre_portes = nombre_portes

    def afficher_details(self):
        super().afficher_details()
        print(f"Nombre de portes: {self.nombre_portes}")

    def freiner(self):
        print(f"{self.marque} {self.modele} utilise la pédale de frein.")

class VoitureElectrique(Electrique):
    def __init__(self, marque, modele, couleur, vitesse_max, capacite_batterie, nombre_portes):
        super().__init__(marque, modele, couleur, vitesse_max, capacite_batterie)
        self.nombre_portes = nombre_portes

    def afficher_details(self):
        super().afficher_details()
        print(f"Nombre de portes: {self.nombre_portes}")

    def freiner(self):
        print(f"{self.marque} {self.modele} utilise la pédale de frein.")

class ScooterThermique(Thermique):
    def __init__(self, marque, modele, couleur, vitesse_max, capacite_reservoir, type_scooter):
        super().__init__(marque, modele, couleur, vitesse_max, capacite_reservoir)
        self.type_scooter = type_scooter

    def afficher_details(self):
        super().afficher_details()
        print(f"Type de scooter: {self.type_scooter}")

    def freiner(self):
        print(f"{self.marque} {self.modele} utilise le frein à main.")

class ScooterElectrique(Electrique):
    def __init__(self, marque, modele, couleur, vitesse_max, capacite_batterie, type_scooter):
        super().__init__(marque, modele, couleur, vitesse_max, capacite_batterie)
        self.type_scooter = type_scooter

    def afficher_details(self):
        super().afficher_details()
        print(f"Type de scooter: {self.type_scooter}")

    def freiner(self):
        print(f"{self.marque} {self.modele} utilise le frein à main.")

# Exemple d'instanciation
voiture1 = VoitureThermique("Toyota", "Corolla", "Rouge", 180, 50, 4)
voiture2 = VoitureElectrique("Tesla", "Model S", "Bleu", 250, 100, 4)
scooter1 = ScooterThermique("Yamaha", "XMAX", "Noir", 120, 13, "Sport")
scooter2 = ScooterElectrique("Vespa", "Elettrica", "Argent", 70, 4, "Urbain")

# Affichage des détails
voiture1.afficher_details()
voiture2.afficher_details()
scooter1.afficher_details()
scooter2.afficher_details()

# Simulation du freinage
voiture1.freiner()
voiture2.freiner()
scooter1.freiner()
scooter2.freiner()
