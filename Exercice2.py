import json
from datetime import datetime

class Serializable:
    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    @classmethod
    def from_json(cls, json_str):
        return cls(**json.loads(json_str))

class Historisable:
    def __init__(self):
        self.historique = []

    def enregistrer_etat(self):
        self.historique.append((datetime.now(), self.__dict__.copy()))

class Journalisable:
    def journaliser(self, message):
        print(f"[Journal] {datetime.now()}: {message}")

class Horodatable:
    def horodatage(self):
        return datetime.now()

class CsvExportable:
    def to_csv(self):
        keys = ";".join(self.__dict__.keys())
        values = ";".join(str(v) for v in self.__dict__.values())
        return keys + "\n" + values

class XmlExportable:
    def to_xml(self):
        items = "".join(f"<{k}>{v}</{k}>" for k, v in self.__dict__.items())
        return f"<objet>{items}</objet>"

class Contrat(Serializable, Historisable, Journalisable, Horodatable, CsvExportable, XmlExportable):
    def __init__(self, id, description):
        Historisable.__init__(self)
        self.id = id
        self.description = description

    def modifier(self, nouvelle_desc):
        self.journaliser(f"Modification du contrat {self.id}")
        self.enregistrer_etat()
        self.description = nouvelle_desc


# Exemple d'utilisation
c = Contrat(1, "Initial")
c.modifier("Révisé")
print(c.to_json())
