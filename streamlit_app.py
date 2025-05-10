import streamlit as st
from datetime import datetime
st.markdown("""
    <style>
        body {
            background-color: #F7E9E9;  
        }    
        [data-testid="stSidebar"] {
            background-color: #12239E;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        /* Style selectbox */
        .stSelectbox > div {
            color: black !important;
            background-color: #0056b3 !important;
        }
    </style>
""", unsafe_allow_html=True)

current_year = datetime.now().year
years = list(range(current_year, 1949, -1))
selected_year = st.sidebar.selectbox("Byggeår:", years)

energy_classes = ['A', 'B', 'C', 'D', 'E', 'F','Ukjent']
selected_energi=st.sidebar.radio("Energikarakter Fra Enova:",energy_classes )

bolig_type=['Boligblokk','Forretningsbygg (handel)','Hotell' ,'Kontorbygg' ,'Lett industri/Verksteder']
selected_bolig=st.sidebar.radio("Bygningstype:",bolig_type )

selected_kwh=['≤ 89,2' ,'89,3 - 102,9','103 - 125,2','125,3 - 148,9' ,'149 - 149,5','149,6 ≤']
selected_bolig=st.sidebar.radio("Beregnet energiforbruk iht energiattest (kWh per kvm per år):",selected_kwh )
