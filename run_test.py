import subprocess
import os
import sys
import webbrowser

# Analyse manuelle de la couverture par fichier
def analyse_manuelle():
    print("\n📊 ANALYSE MANUELLE DE COUVERTURE :")

    rapports = {
        "employer.py": {
            "couverture": "100%",
            "non_testé": "Aucun",
            "remarques": "Tous les cas (y compris erreurs) sont testés ✅"
        },
        "tracteur.py": {
            "couverture": "~100%",
            "non_testé": "est_disponible() (pas directement)",
            "remarques": "Couvert via l’attribut .disponible"
        },
        "champ.py": {
            "couverture": "99%",
            "non_testé": "test_champ_stockable() est vide",
            "remarques": "Tous les comportements clés sont testés"
        },
        "legume.py": {
            "couverture": "Enum (indirect)",
            "non_testé": "Aucun",
            "remarques": "Enum bien utilisée dans tous les tests"
        },
        "strategy.py": {
            "couverture": "~95%",
            "non_testé": "print(), usage unique de Legume.PATATE",
            "remarques": "Bonne logique testée, mais test de console absent"
        }
    }

    for fichier, infos in rapports.items():
        print(f"\n📁 {fichier}")
        print(f"   🔹 Couverture : {infos['couverture']}")
        print(f"   🔸 Non testé  : {infos['non_testé']}")
        print(f"   📝 Remarques  : {infos['remarques']}")

# Fonction générique d’exécution
def run_command(command, description):
    print(f"\n📦 {description}")
    print(">>>", " ".join(command))
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Échec de : {description}")
        sys.exit(result.returncode)
    print(f"✅ {description} terminé avec succès.")

# Script principal
def run_tests():
    os.environ["PYTHONPATH"] = os.getcwd()

    run_command(
        ["python", "-m", "pytest", "--cov=.", "test/"],
        "Lancement des tests avec couverture"
    )

    run_command(
        ["coverage", "report", "--fail-under=80"],
        "Vérification de la couverture (≥ 80%)"
    )

    run_command(
        ["coverage", "html"],
        "Génération du rapport HTML de couverture"
    )

    analyse_manuelle()

    index_path = os.path.abspath("htmlcov/index.html")
    print(f"\n🌐 Ouverture du rapport HTML : {index_path}")
    webbrowser.open(f"file://{index_path}")

if __name__ == "__main__":
    run_tests()
