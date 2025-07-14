# 📊 Rostaing Reporting (RR) - Votre Assistant d'Analyse de Données Automatisé

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Framework](https://img.shields.io/badge/Framework-Streamlit-red.svg)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Dependencies](https://img.shields.io/badge/Dependencies-Pandas-brightgreen.svg)](https://pandas.pydata.org/)
[![Rostaing Report]](https://pypi.org/project/rostaing-report/)

**Rostaing Reporting** est une application web puissante et intuitive conçue avec Python et Streamlit. Elle automatise le processus fastidieux de l'analyse exploratoire des données (EDA). Chargez simplement votre fichier de données, et laissez l'application générer des rapports détaillés, des visualisations et des tests statistiques en quelques clics.

Fini les notebooks Jupyter répétitifs, place à l'analyse interactive et efficace !

## 🚀 Fonctionnalités Principales

*   **📤 Chargement de Données Multi-formats :** Importez facilement vos données via des fichiers `.csv`, `.xlsx` (Excel), ou `.json`.
*   **📈 Analyse Exploratoire Automatisée (EDA) :** Générez un rapport complet qui inclut :
    *   Vue d'ensemble des données (nombre de variables, observations, valeurs manquantes).
    *   Analyse détaillée pour chaque variable (distribution, statistiques clés, etc.).
    *   Analyse des interactions et corrélations entre les variables.
*   **📊 Interface de Données Interactive :** Visualisez vos données dans un tableau complet ou via un système de pagination pour une meilleure performance sur les grands jeux de données.
*   **🔬 Tests Statistiques à la Demande :** Réalisez des tests statistiques complexes sans écrire une seule ligne de code :
    *   **Test du Chi-carré (χ²) :** Pour tester l'indépendance entre deux variables catégorielles.
    *   **Test de Kolmogorov-Smirnov (K-S) :** Pour comparer la distribution d'une variable à une loi normale.
    *   **Test de Mann-Whitney U :** Pour comparer les distributions de deux groupes indépendants.
    *   **Test de Normalité (Shapiro-Wilk) :** Pour vérifier si une variable suit une distribution normale.
*   **📥 Export Facile :**
    *   Téléchargez le rapport d'analyse complet au format **HTML**.
    *   Exportez la vue actuelle du dashboard en **PNG** ou **PDF** pour vos présentations.
    *   Téléchargez les résultats des tests statistiques au format **CSV**.
*   **🧹 Interface Propre et Réutilisable :** Un bouton "Nettoyer et recommencer" permet de réinitialiser l'application pour une nouvelle analyse.

## 🛠️ Technologies Utilisées

*   **Backend & Logique :** Python
*   **Interface Web :** Streamlit
*   **Manipulation de Données :** Pandas, Numpy
*   **Tests Statistiques :** Scipy
*   **Lecture de Fichiers Excel :** openpyxl
*   **Génération de Rapport :** rostaing-report

## ⚙️ Installation et Lancement

Suivez ces étapes pour lancer le projet sur votre machine locale.

### 1. Prérequis

*   [Python 3.8+](https://www.python.org/downloads/)
*   `pip` (généralement inclus avec Python)
*   [Git](https://git-scm.com/downloads)

### 2. Instructions d'Installation

1.  **Clonez le dépôt :**
    ```bash
    git clone https://github.com/VOTRE_NOM_UTILISATEUR/VOTRE_REPO.git
    cd VOTRE_REPO
    ```

2.  **Créez un environnement virtuel (recommandé) :**
    *   Sur macOS/Linux :
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   Sur Windows :
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Installez les dépendances :**
    Créez un fichier `requirements.txt` à la racine de votre projet avec le contenu suivant, puis lancez la commande.

    **`requirements.txt`**
    ```bash
    numpy==2.3.1
    pandas==2.3.1
    rostaing_report==0.1.2
    streamlit==1.46.1
    streamlit_nightly==1.38.1.dev20240830
    ```

    **Commande d'installation :**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Lancement de l'application

Une fois les dépendances installées, lancez l'application avec la commande suivante (en supposant que votre fichier principal s'appelle `app.py`) :

```bash
streamlit run app.py
```