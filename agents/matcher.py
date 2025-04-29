suppliers = {
    "rPET": ["Loop Industries", "Veolia"],
    "bioPET": ["Avantium", "Anellotech"],
}

def get_suppliers(material):
    return suppliers.get(material, [])