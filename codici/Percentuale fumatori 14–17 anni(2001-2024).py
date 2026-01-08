import plotly.express as px
import pandas as pd
import os

file_name = "/content/drive/MyDrive/Visualizzazione/Fumatori14-17anni_barreverticali.csv"

def generate_bar_chart():

    # Controllo file
    if not os.path.exists(file_name):
        print(f"ERRORE: Il file '{file_name}' non è stato trovato.")
        return

    try:
        # Caricamento dati
        df_raw = pd.read_csv(file_name)

        # Filtraggio (fumatori SI + percentuale)
        mask = (
            (df_raw['DATA_TYPE'] == '14_FUMO_SI') &
            (df_raw['MEASURE'] == 'HSC') &
            (df_raw['AGE'] == 'Y14-17')
        )

        df = df_raw[mask].copy()

        if df.empty:
            print("Nessun dato trovato con i filtri impostati.")
            return

        # Conversione colonne
        df['TIME_PERIOD'] = pd.to_numeric(df['TIME_PERIOD'], errors='coerce')
        df['Osservazione'] = pd.to_numeric(df['Osservazione'], errors='coerce')
        df.dropna(subset=['TIME_PERIOD', 'Osservazione'], inplace=True)

        df = df.sort_values("TIME_PERIOD")

        # Grafico a barre verticali
        fig = px.bar(
            df,
            x='TIME_PERIOD',
            y='Osservazione',
            text='Osservazione',
            labels={
                'TIME_PERIOD': 'Anno',
                'Osservazione': 'Fumatori (%)'
            },
            title='<b>Percentuale fumatori 14–17 anni (2001–2024)</b><br>Dati ISTAT'
        )

        # Layout
        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig.update_layout(
            font=dict(family="Arial", size=14),
            yaxis_range=[0, df["Osservazione"].max() + 4]
        )

        fig.show()

    except Exception as e:
        print(f"Errore durante l'elaborazione: {e}")


generate_bar_chart()