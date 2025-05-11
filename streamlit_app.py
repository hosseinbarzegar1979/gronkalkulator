import streamlit as st
from datetime import datetime

def coalesce_not_blank(*args):
    return next((x for x in args if x not in [None, ""]), None)


st.title("📊 Grønt Næringseiendom")

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
        /* Specifically target the selectbox */
        .stSelectbox div, .stSelectbox select {
            color: black !important;
          
        }

        /* Override selected item font color */
        .stSelectbox select option {
            color: black !important;
   
        }

        .bottom-right-image {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 9999;
    }       
                  
    </style>
    <img src="https://merkevare.sparebank1.no/readimage.aspx/asset.png?pubid=CW58YbnnvOMw09ffMi6Wwg"
        class="bottom-right-image" width="100">       
""", unsafe_allow_html=True)

current_year = datetime.now().year
years = list(range(current_year, 1949, -1))
selected_year = st.sidebar.selectbox("Byggeår:", years)

energy_classes = [None,'A', 'B', 'C', 'D', 'E', 'F','Ukjent']
selected_energi=st.sidebar.radio("Energikarakter Fra Enova:",energy_classes,format_func=lambda x: "Velg..." if x is None else x )

bolig_type=[None, 'Boligblokk','Forretningsbygg (handel)','Hotell' ,'Kontorbygg' ,'Lett industri/Verksteder']
nzeb_maksimalgrense=[0,76,113,67,159,162]
fastledd_list=[0,34.5,23.5,28.9,5.8,3.7]
selected_bolig=st.sidebar.radio("Bygningstype:",bolig_type,format_func=lambda x: "Velg..." if x is None else x )

kwh=[None,'≤ 89,2' ,'89,3 - 102,9','103 - 125,2','125,3 - 148,9' ,'149 - 149,5','149,6 ≤']
overg_grense=[0,89,2,102.9,125.2,148.9,149.5,150]

selected_kwh=st.sidebar.radio("Beregnet energiforbruk iht energiattest (kWh per kvm per år):",kwh,format_func=lambda x: "Velg..." if x is None else x )


byggeaar = selected_year
bygningstype =selected_bolig
energikarakter = selected_energi
if selected_kwh !="":
    indx=kwh.index(selected_kwh)
    beregnet_levert_energi=overg_grense[indx]
else :
    beregnet_levert_energi=None

if bolig_type is not None:
    indx=bolig_type.index(selected_bolig)
    NZEB_maks=nzeb_maksimalgrense[indx]
    fastledd=fastledd_list[indx]
else:
    NZEB_maks=None
    fastledd=None




if (byggeaar is None) and (energikarakter is None) and (beregnet_levert_energi) and (bygningstype):
        allFieldsEmpty=True
else:
        allFieldsEmpty=False


if  byggeaar < 2012 and  (energikarakter is None):
    utenkarakter_for_2012="Fyll inn energikarakter"
else:
    utenkarakter_for_2012=""



if  byggeaar >= 2021 and  ( (bygningstype is None) or (beregnet_levert_energi is None)) :
    byggeaar2021_uten_info="Vennligst fyll inn bygningstype og beregnet levert energi iht energiattest"
else:
    byggeaar2021_uten_info=""



if ( byggeaar >= 2012 and byggeaar < 2021  and  ( byggeaar is not  None) ) or (byggeaar < 2012  and energikarakter in {"A", "B"}) :
    Topp_15="Taksonomigrønn iht topp 15%-definisjonen"
else:
    Topp_15=""

if Topp_15 == "" and byggeaar >= 2021 and  bygningstype == "Leilighet" and  (beregnet_levert_energi is not None):
        if (beregnet_levert_energi <= NZEB_maks*0.9+fastledd):
            NZEB_10_leilighet= "Bygningen er taksonomigrønn iht NZEB-10 definisjon"
        else:
            NZEB_10_leilighet="Bygningen er ikke taksonomigrønn. For å bli grønn må energiforbruket reduseres til under 89,3 kWh per kvadratmeter per år."
else:
        NZEB_10_leilighet=""




if Topp_15 == "" and NZEB_10_leilighet=="" and byggeaar >= 2021 and  bygningstype == "Kontorbygg" and  (beregnet_levert_energi is not None):
        if (beregnet_levert_energi <= NZEB_maks*0.9+fastledd):
            NZEB_10_kontorbygg= "Bygningen er taksonomigrønn iht NZEB-10 definisjon"
        else:
            NZEB_10_kontorbygg="Bygningen er ikke taksonomigrønn. For å bli grønn må energiforbruket reduseres til under 103 kWh per kvadratmeter per år."
else:
        NZEB_10_kontorbygg=""



if Topp_15 == "" and NZEB_10_leilighet=="" and NZEB_10_kontorbygg=="" and byggeaar >= 2021 and  bygningstype == "Lett industri/verksteder" and  (beregnet_levert_energi is not None):
        if (beregnet_levert_energi <= NZEB_maks*0.9+fastledd):
            NZEB_10_industri= "Bygningen er taksonomigrønn iht NZEB-10 definisjon"
        else:
            NZEB_10_industri="Bygningen er ikke taksonomigrønn. For å bli grønn må energiforbruket reduseres til under 125,3 kWh per kvadratmeter per år."
else:
        NZEB_10_industri=""




if Topp_15 == "" and NZEB_10_leilighet=="" and NZEB_10_kontorbygg=="" and NZEB_10_industri=="" and byggeaar >= 2021 and  bygningstype == "Boligblokk" and  (beregnet_levert_energi is not None):
        if (beregnet_levert_energi <= NZEB_maks*0.9+fastledd):
            NZEB_10_boligblokk= "Bygningen er taksonomigrønn iht NZEB-10 definisjon"
        else:
            NZEB_10_boligblokk="Bygningen er ikke taksonomigrønn. For å bli grønn må energiforbruket reduseres til under 89,3 kWh per kvadratmeter per år."
else:
        NZEB_10_boligblokk=""


if Topp_15 == "" and NZEB_10_leilighet=="" and NZEB_10_kontorbygg=="" and NZEB_10_industri=="" and NZEB_10_boligblokk=="" and byggeaar >= 2021 and  bygningstype == "Boligblokk" and  (beregnet_levert_energi is not None):
        if (beregnet_levert_energi <= NZEB_maks*0.9+fastledd):
            NZEB_10_hotell= "Bygningen er taksonomigrønn iht NZEB-10 definisjon"
        else:
            NZEB_10_hotell="Bygningen er ikke taksonomigrønn. For å bli grønn må energiforbruket reduseres til under 149 kWh per kvadratmeter per år."
else:
        NZEB_10_hotell=""



if Topp_15 == "" and NZEB_10_leilighet=="" and NZEB_10_kontorbygg=="" and NZEB_10_industri=="" and NZEB_10_boligblokk=="" and NZEB_10_hotell=="" and byggeaar >= 2021 and  bygningstype == "Boligblokk" and  (beregnet_levert_energi is not None):
        if (beregnet_levert_energi <= NZEB_maks*0.9+fastledd):
            NZEB_10_forretning= "Bygningen er taksonomigrønn iht NZEB-10 definisjon"
        else:
            NZEB_10_forretning="Bygningen er ikke taksonomigrønn. For å bli grønn må energiforbruket reduseres til under 149,6 kWh per kvadratmeter per år."
else:
        NZEB_10_forretning=""

final_nzeb=""
final_nzeb=coalesce_not_blank(NZEB_10_leilighet,NZEB_10_kontorbygg,NZEB_10_industri,NZEB_10_boligblokk,NZEB_10_forretning)
    


if (allFieldsEmpty==True ) :
         st.warning("⚠️ Vennligst fyll inn bygningens byggeår, og annen relevant info.")
else :
         if   byggeaar2021_uten_info !="" :
              st.warning("⚠️ " + byggeaar2021_uten_info)   
         else:
             if Topp_15 !="" :
                  st.success("🏡 " + Topp_15)
             else:
                if final_nzeb is not None:
                   if final_nzeb=="Bygningen er taksonomigrønn iht NZEB-10 definisjon":
                    st.success("🏡 " + final_nzeb) 
                   else :
                    st.warning("⚠️ "+  final_nzeb)   
                else:
                    st.warning("⚠️ " + "Ikke taksonomigrønn. For å bli grønn må eiendommen ha energimerke A eller B.")        
                



