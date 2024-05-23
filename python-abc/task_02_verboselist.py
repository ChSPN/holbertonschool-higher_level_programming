#!/usr/bin/env python3
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Ajouté [{item}] à la liste.")

    def extend(self, items):
        super().extend(items)
        print(f"Étendu la liste avec [{len(items)}] éléments.")

    def remove(self, item):
        if item in self:
            super().remove(item)
            print(f"Supprimé [{item}] de la liste.")
        else:
            print(f"Élément [{item}] non trouvé dans la liste.")

    def pop(self, index=-1):
        if len(self) > 0:
            item = super().pop(index)
            print(f"Retiré [{item}] de la liste.")
        else:
            print("Aucun élément à retirer de la liste.")
