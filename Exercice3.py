from datetime import datetime
import copy

class ValidationMixin:
    def valider_titre(self):
        if not getattr(self, "titre", None):
            raise ValueError("Le titre doit être renseigné et non vide.")

class HistoriqueMixin:
    def __init__(self):
        self._historique = []

    def enregistrer_version(self):
        self._historique.append({
            "timestamp": datetime.now(),
            "ancienne_description": copy.deepcopy(self.description)
        })

    def afficher_historique(self):
        for entry in self._historique:
            print(f"[{entry['timestamp']}] {entry['ancienne_description']}")

class JournalisationMixin:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()} : {message}")

class Tache(ValidationMixin, HistoriqueMixin, JournalisationMixin):
    def __init__(self, titre, description):
        HistoriqueMixin.__init__(self)
        self.titre = titre
        self.description = description
        self.date_creation = datetime.now()
        self.valider_titre()
        self.journaliser(f"Tâche créée : {self.titre}")

    def mettre_a_jour(self, nouvelle_description):
        self.valider_titre()
        self.enregistrer_version()
        self.description = nouvelle_description
        self.journaliser(f"Description mise à jour pour : {self.titre}")
