import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
import streamlit.components.v1 as components
import math
from datetime import datetime

try:
    from rostaing import rostaing_report
except ImportError:
    st.error("Erreur critique : La bibliothèque 'rostaing_report' n'a pas pu être importée. Assurez-vous que le fichier rostaing.py est dans le même répertoire ou que la bibliothèque est correctement installée.")
    st.stop()

# --- Configuration de la page ---
st.set_page_config(
    page_title="Rostaing Reporting",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Fonctions Utilitaires ---

@st.cache_data
def load_data(uploaded_file):
    """Charge les données depuis un fichier téléversé dans un DataFrame Pandas."""
    try:
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xls', '.xlsx')):
            return pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('.json'):
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            return pd.read_json(stringio)
        else:
            st.error("Format de fichier non supporté. Veuillez utiliser un fichier CSV, Excel ou JSON.")
            return None
    except Exception as e:
        st.error(f"Une erreur est survenue lors de la lecture du fichier : {e}")
        return None
        
@st.cache_data
def convert_df_to_csv(df):
    """Convertit un DataFrame en CSV encodé en UTF-8 pour le téléchargement."""
    return df.to_csv(index=True).encode('utf-8')

def add_export_buttons():
    """Injecte du HTML/JS pour les boutons d'export PDF et Image."""
    js_code = """
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"></script>
    <script>
        // Fonction pour attendre que les images (graphiques) soient chargées
        const waitForImages = async (element) => {
            const images = Array.from(element.getElementsByTagName('img'));
            const promises = images.map(img => {
                if (img.complete) return Promise.resolve();
                return new Promise(resolve => {
                    img.onload = img.onerror = resolve;
                });
            });
            await Promise.all(promises);
        };

        async function exportToImage() {
            const element = document.getElementById('printable_area');
            await waitForImages(element); // Attendre que les images soient prêtes
            html2canvas(element, {
                scale: 2,
                useCORS: true,
                backgroundColor: '#FFFFFF'
            }).then(canvas => {
                var link = document.createElement('a');
                link.download = 'rostaing_report.png';
                link.href = canvas.toDataURL('image/png');
                link.click();
            });
        }

        async function exportToPDF() {
            const element = document.getElementById('printable_area');
            await waitForImages(element); // Attendre que les images soient prêtes
            const opt = {
                margin:       [0.5, 0.2, 0.5, 0.2],
                filename:     'rostaing_report.pdf',
                image:        { type: 'jpeg', quality: 0.95 },
                html2canvas:  { scale: 2, useCORS: true, letterRendering: true },
                jsPDF:        { unit: 'in', format: 'a4', orientation: 'portrait' }
            };
            html2pdf().from(element).set(opt).save();
        }
    </script>
    """
    
    # Style pour que nos boutons HTML ressemblent aux boutons de Streamlit
    button_style = """
    <style>
        .export-btn {
            background-color: #FFFFFF;
            color: #0d1117;
            border: 1px solid rgba(49, 51, 63, 0.2);
            border-radius: 0.5rem;
            padding: 0.4rem 0.8rem;
            font-size: 14px;
            font-weight: 400;
            margin: 0;
            cursor: pointer;
            width: 100%;
            display: inline-flex;
            align-items: center;
            justify-content: center;
        }
        .export-btn:hover {
            border-color: #0072B2;
            color: #0072B2;
        }
        .export-btn:active {
            background-color: #f0f2f6;
        }
    </style>
    """
    st.markdown(js_code + button_style, unsafe_allow_html=True)
    
# --- État de la Session ---
if 'df' not in st.session_state:
    st.session_state.df = None
if 'report' not in st.session_state:
    st.session_state.report = None

# --- Sidebar ---
with st.sidebar:
    st.image("https://placehold.co/300x100/0072B2/FFFFFF?text=Rostaing+Reporting (RR)&font=roboto", use_container_width=True)
    # st.title("Configuration")
    # st.markdown("---")
    
    uploaded_file = st.file_uploader(
        "**1. Téléversez votre fichier de données**",
        type=['csv', 'xlsx', 'xls', 'json'],
        help="Formats supportés : CSV, Excel, JSON."
    )

    if uploaded_file is not None:
        if st.button("**2. Analyser les données**", use_container_width=True, type="primary"):
            with st.spinner("Chargement et analyse des données en cours..."):
                df = load_data(uploaded_file)
                if df is not None:
                    st.session_state.df = df
                    st.session_state.report = rostaing_report(df)
                    st.success("Analyse terminée avec succès !")

    # ==============================================================================
    # BOUTON DE NETTOYAGE
    # ==============================================================================
    # Ce bloc n'apparaît que si une analyse a déjà été effectuée.
    if st.session_state.df is not None:
        st.markdown("---")
        if st.button("🧹 Nettoyer et recommencer", use_container_width=True):
            # Réinitialisation des variables de session qui contiennent les données et le rapport
            st.session_state.df = None
            st.session_state.report = None
            # On force le rechargement de la page pour rafraîchir l'interface
            st.rerun()
    # ==============================================================================
    # FIN DU BOUTON DE NETTOYAGE
    # ==============================================================================

    st.markdown("---")
    st.info("Cette application génère une analyse exploratoire des données (EDA) et permet d'effectuer des tests statistiques interactifs.")


# --- Contenu Principal de l'Application ---
st.title("📊 RR : Votre Assistant d'Analyse de Données")
st.markdown("Bienvenue sur la plateforme d'analyse de données interactive. **Commencez par téléverser un fichier dans la barre latérale gauche.**")

if st.session_state.df is not None:
    
    df = st.session_state.df
    report = st.session_state.report

    # Ajout des boutons d'exportation
    add_export_buttons()
    st.markdown("<hr>", unsafe_allow_html=True)

    # Nous enveloppons tout le contenu à exporter dans un div avec un ID spécifique
    st.markdown('<div id="printable_area">', unsafe_allow_html=True)
    
    # --- Section 1: Exploration des Données avec choix d'affichage ---
    st.header("1. Exploration des Données Chargées")
    st.markdown(f"**Dimensions des données :** `{df.shape[0]}` lignes et `{df.shape[1]}` colonnes.")
    
    tab_full, tab_paginated = st.tabs(["Affichage Complet", "Affichage Paginé"])

    with tab_full:
        st.dataframe(df)
        st.caption("Affichage de l'ensemble des données. Peut être lent pour de très grands fichiers.")

    with tab_paginated:
        col1, col2 = st.columns(2)
        with col1:
            rows_per_page = st.number_input("Lignes par page", min_value=5, max_value=100, value=10, step=5, key='rows_per_page')
        total_pages = math.ceil(len(df) / rows_per_page)
        with col2:
            page_number = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1, key='page_number')
        
        start_idx = (page_number - 1) * rows_per_page
        end_idx = min(start_idx + rows_per_page, len(df))
        st.dataframe(df.iloc[start_idx:end_idx])
        st.caption(f"Affichage des lignes {start_idx+1} à {end_idx} sur un total de {len(df)}.")
    
    # --- Section 2: Rapport d'Analyse Exploratoire (EDA) ---
    st.header("2. Rapport d'Analyse Exploratoire Complet")
    html_report, report_as_string = None, None
    try:
        if hasattr(report, 'to_html') and callable(getattr(report, 'to_html')): html_report = report.to_html()
        elif hasattr(report, '_repr_html_') and callable(getattr(report, '_repr_html_')): html_report = report._repr_html_()
        else: report_as_string = str(report)
    except Exception as e:
        st.warning(f"Impossible de générer le rapport HTML. Erreur : {e}"); report_as_string = str(report)

    if html_report:
        st.download_button(label="📥 Télécharger le Rapport HTML", data=html_report, file_name="rostaing_report.html", mime="text/html")
        components.html(html_report, height=800, scrolling=True)
    elif report_as_string:
        st.download_button(label="📥 Télécharger le Rapport Texte", data=report_as_string, file_name="rostaing_report.txt", mime="text/plain")
        st.code(report_as_string, language='text')

    # --- Section 3: Tests Statistiques Interactifs ---
    st.header("3. Tests Statistiques Interactifs")
    all_columns = df.columns.tolist()
    numeric_columns = df.select_dtypes(include=np.number).columns.tolist()
    
    tab1, tab2, tab3, tab4 = st.tabs(["Test du Chi-carré (χ²)", "Test K-S", "Test Mann-Whitney U", "Test de Normalité"])

    with tab1:
        st.info("Vérifie l'indépendance entre deux variables catégorielles.")
        c1, c2 = st.columns(2); var1 = c1.selectbox("Variable 1", all_columns, key='c1_chi'); var2 = c2.selectbox("Variable 2", all_columns, key='c2_chi')
        if st.button("Exécuter Test Chi-carré", key='b_chi'):
            if var1 and var2 and var1 != var2:
                try:
                    with st.spinner("Calcul en cours..."):
                        chi2_res = report.chi2_test(var1, var2)
                        res_df = pd.DataFrame.from_dict(chi2_res, orient='index', columns=['Valeur'])
                        st.dataframe(res_df)
                        st.download_button("📥 Télécharger (CSV)", convert_df_to_csv(res_df), f"chi2_{var1}_vs_{var2}.csv", 'text/csv')
                except Exception as e: st.error(f"Erreur : {e}")
            else: st.warning("Sélectionnez deux variables différentes.")
    
    with tab2:
        st.info("Compare une variable à une distribution normale.")
        ks_var = st.selectbox("Variable numérique", numeric_columns, key='ks_var')
        if st.button("Exécuter Test K-S", key='ks_btn'):
            if ks_var:
                try:
                    with st.spinner("Calcul en cours..."):
                        ks_res = report.ks_test(ks_var, dist='norm')
                        res_df = pd.Series(ks_res).to_frame('Valeur')
                        st.dataframe(res_df)
                        st.download_button("📥 Télécharger (CSV)", convert_df_to_csv(res_df), f"ks_test_{ks_var}.csv", 'text/csv')
                except Exception as e: st.error(f"Erreur : {e}")
            else: st.warning("Sélectionnez une variable.")

    with tab3:
        st.info("Compare les distributions de deux groupes indépendants.")
        c1, c2 = st.columns(2)
        mw_var = c1.selectbox("Variable numérique", numeric_columns, key='mw_var')
        group_var = c2.selectbox("Variable de groupe", all_columns, key='mw_group')
        if st.button("Exécuter Test Mann-Whitney U", key='mw_btn'):
            if mw_var and group_var:
                if df[group_var].nunique() != 2: st.warning(f"'{group_var}' doit avoir 2 catégories uniques.")
                try:
                    with st.spinner("Calcul en cours..."):
                        mw_res = report.mann_whitney_u_test(col=mw_var, group_col=group_var)
                        res_df = pd.Series(mw_res).to_frame('Valeur')
                        st.dataframe(res_df)
                        st.download_button("📥 Télécharger (CSV)", convert_df_to_csv(res_df), f"mann_whitney_{mw_var}_by_{group_var}.csv", 'text/csv')
                except Exception as e: st.error(f"Erreur : {e}")
            else: st.warning("Sélectionnez les deux variables.")

    with tab4:
        st.info("Teste si une variable suit une loi normale.")
        norm_var = st.selectbox("Variable numérique", numeric_columns, key='norm_var_2')
        if st.button("Exécuter Test de Normalité", key='norm_btn'):
            if norm_var:
                try:
                    with st.spinner("Calcul en cours..."):
                        norm_res = report.normality_test(norm_var, test='shapiro')
                        res_df = pd.Series(norm_res).to_frame('Valeur')
                        st.dataframe(res_df)
                        st.download_button("📥 Télécharger (CSV)", convert_df_to_csv(res_df), f"shapiro_test_{norm_var}.csv", 'text/csv')
                except Exception as e: st.error(f"Erreur : {e}")
            else: st.warning("Sélectionnez une variable.")

    st.markdown('</div>', unsafe_allow_html=True) # Fermeture du div exportable
        
# --- Pied de Page ---
st.markdown("---")
current_date = datetime.now().year
st.markdown(
    f"""
    <div style="text-align: center; color: grey;">
        <p>Rostaing Reporting © {current_date}</p>
    </div>
    """,
    unsafe_allow_html=True
)