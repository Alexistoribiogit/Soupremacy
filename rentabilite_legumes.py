import random
import pandas as pd

def simulate_legume(culture, base_price=3000, irrigation_cost=10, harvest_days=2, total_days=365):
    """Simule la rentabilité d'un légume sur une année."""
    champ_cost = 10000  # Coût d'achat d'un champ
    irrigation_count = 10  # Nombre d'arrosages requis
    irrigation_price = irrigation_count * irrigation_cost  # Coût total d'arrosage
    
    # Calcul du prix de vente en fonction de la concurrence
    concurrent_fields = random.randint(0, 20)  # Simulation du nombre d'autres champs cultivant le même légume
    selling_price = max(500, base_price - 50 * concurrent_fields)  # Prix minimum de 500€
    
    # Nombre de cycles possibles en un an (chaque cycle prend environ 15 jours)
    cycle_days = irrigation_count + harvest_days
    num_cycles = total_days // cycle_days
    
    # Calcul du bénéfice annuel
    total_revenue = num_cycles * selling_price
    total_costs = champ_cost + (num_cycles * irrigation_price)
    profit = total_revenue - total_costs
    
    return {
        "Légume": culture,
        "Revenu Total (€)": total_revenue,
        "Coût Total (€)": total_costs,
        "Profit (€)": profit,
        "Cycles par an": num_cycles,
        "Prix de vente moyen (€)": selling_price,
    }

# Légumes disponibles
legumes = {
    "PATATE": 3000,
    "POIREAU": 3200,
    "TOMATE": 3500,
    "OIGNON": 2800,
    "COURGETTE": 3300,
}

# Simulation pour chaque légume
results = [simulate_legume(legume, base_price) for legume, base_price in legumes.items()]

# Affichage des résultats
df = pd.DataFrame(results)
print(df.to_string(index=False))

# Enregistrement dans un fichier CSV
df.to_csv("rentabilite_legumes.csv", index=False)
print("Les résultats ont été enregistrés dans rentabilite_legumes.csv")
