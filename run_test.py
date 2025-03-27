import subprocess
import os
import sys

def run_command(command, description):
    print(f"\n📦 {description}")
    print(">>>", " ".join(command))
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"❌ Échec de : {description}")
        sys.exit(result.returncode)
    print(f"✅ {description} terminé avec succès.")

def run_tests():
    # Ajouter le dossier courant au PYTHONPATH
    os.environ["PYTHONPATH"] = "."

    # Étape 1 : pytest avec coverage
    run_command(
        ["python", "-m", "pytest", "--cov", "test/"],
        "Lancement des tests avec couverture"
    )

    # Étape 2 : rapport coverage avec seuil 80%
    run_command(
        ["coverage", "report", "--fail-under=80"],
        "Vérification de la couverture (≥ 80%)"
    )

if __name__ == "__main__":
    run_tests()
