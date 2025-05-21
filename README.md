# 🧠 Delphos — Système d'Aide à la Décision pour le Trading Forex

**Delphos** est un projet de trading systématique personnel conçu pour assister le trader dans ses prises de décision sur le marché du **Forex**, à l’aide d’outils techniques, quantitatifs, et d’analyse macroéconomique.  
Ce système a pour ambition d’offrir des **signaux clairs**, une gestion des **risques rigoureuse**, et une architecture modulaire permettant une évolution progressive vers l'automatisation partielle.

---

## 📁 Architecture du projet

delphos/
│
├── setup.sh # Script d’installation (env virtuel + dépendances)
├── requirements.txt # Liste des packages Python
├── .gitignore # Exclut .venv et fichiers inutiles
│
├── main.py # Script principal d’exécution
├── config.py # Paramètres de configuration globaux
│
├── macro/ # Études fondamentales (manuel)
│ └── notes.md # Résumés d’articles, analyses macro
│
├── tech_analysis/ # Module technique
│ ├── indicators.py # RSI, SMA, supports/résistances
│ └── signal_engine.py # Système de génération de signaux
│
├── quant_analysis/ # Module quantitatif
│ ├── correlation.py # Corrélations entre paires Forex
│ └── volatility.py # Volatilité, bandes, graphiques
│
├── risk_management/ # Module de gestion du risque
│ └── position_sizing.py # Taille de position recommandée
│
├── alerts/ # Système de notifications (à venir)
│ └── notifier.py
│
└── reports/ # Historique des signaux/logs
└── logs_signaux.csv

---

## 🚀 Installation

### 1. Clone le projet

```bash
git clone https://github.com/<ton-utilisateur>/delphos.git
cd delphos
```

### Rendre executable

```
chmod +x setup.sh
./setup.sh
```

### Executer le fichier

`source .venv/bin/activate`
