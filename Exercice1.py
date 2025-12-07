from datetime import datetime
import json
from abc import ABC, abstractmethod

class Horodatable:
    def horodatage(self):
        print(f"[LOG] Action à {datetime.now()}")

class Serializable:
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False, indent=4)

class Historisable:
    def __init__(self, *args, **kwargs):
        self._historique = []
        super().__init__(*args, **kwargs)

    def ajouter_historique(self, action):
        timestamp = datetime.now()
        self._historique.append((timestamp, action))
        print(f"[HIST] {action} — {timestamp}")

    def afficher_historique(self):
        for t, a in self._historique:
            print(f"{t} — {a}")

class Validable(ABC):
    @abstractmethod
    def get_contenu_a_valider(self):
        pass

    def valider(self):
        if not self.get_contenu_a_valider():
            raise ValueError("Contenu invalide")
        print("Validation OK")

class Document(Historisable, Horodatable, Validable, Serializable):
    def __init__(self, titre, contenu):
        super().__init__()
        self.titre = titre
        self.contenu = contenu

    def get_contenu_a_valider(self):
        return self.titre

    def sauvegarder(self):
        self.horodatage()
        self.ajouter_historique("Sauvegarde")
        self.valider()
        print(f"Document '{self.titre}' sauvegardé.")
