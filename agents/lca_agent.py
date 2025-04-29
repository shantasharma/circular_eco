def estimate_emissions(material):
    emissions_kgco2 = {
        "PET": 2.7,
        "rPET": 1.4,
        "bioPET": 1.9,
    }
    return emissions_kgco2.get(material, None)