import plotly.express as px
import pandas as pd
import os

file_name = "/content/drive/MyDrive/Visualizzazione/Fumatori2001-2024_linee.csv"

def generate_line_chart():

    # Verifica presenza file
    if not os.path.exists(file_name):
        print(f"ERRORE: Il file '{file_name}' non è stato trovato.")
        return

    try:
        # Caricamento dati
        df_raw = pd.read_csv(file_name)

        # Filtraggio dati: fumatori (DATA_TYPE = 14_FUMO_SI) e misura percentuale (HSC)
        mask = (
            (df_raw['DATA_TYPE'] == '14_FUMO_SI') &
            (df_raw['MEASURE'] == 'HSC')
        )

        df = df_raw[mask].copy()

        if df.empty:
            print("Nessun dato trovato con i filtri impostati.")
            return

        # Conversione colonne numeriche
        df['TIME_PERIOD'] = pd.to_numeric(df['TIME_PERIOD'], errors='coerce')
        df['Osservazione'] = pd.to_numeric(df['Osservazione'], errors='coerce')
        df.dropna(subset=['TIME_PERIOD', 'Osservazione'], inplace=True)

        # Creazione grafico a linee
        fig = px.line(
            df,
            x='TIME_PERIOD',
            y='Osservazione',
            color='AGE',  
            markers=True,
            labels={
                'TIME_PERIOD': 'Anno',
                'Osservazione': 'Fumatori (%)',
                'AGE': 'Fascia d’età'
            },
            title='<b>Andamento dei fumatori per fascia d’età (2001–2024)</b><br>Dati ISTAT'
        )

        #Layout
        fig.update_layout(
          font=dict(family="Arial", size=14),
          legend_title_text="Fascia d’età",
          hovermode="x unified",
          legend=dict(
            orientation="v",
            x=1.02,
            y=1,
            xanchor="left",
            yanchor="top"
          ),
          margin=dict(r=180)   
        )


        fig.show()

    except Exception as e:
        print(f"Errore durante l'elaborazione: {e}")


generate_line_chart()