import plotly.express as px
import pandas as pd
import os

file_name = "/content/drive/MyDrive/Visualizzazione/Fumatori&non14-17_area.csv"

def generate_area_chart():

    if not os.path.exists(file_name):
        print(f"ERRORE: Il file '{file_name}' non è stato trovato.")
        return

    try:
        # 1. Caricamento dati
        df = pd.read_csv(file_name)

        # 2. Conversione numerica
        df["TIME_PERIOD"] = pd.to_numeric(df["TIME_PERIOD"], errors="coerce")
        df["Osservazione"] = pd.to_numeric(df["Osservazione"], errors="coerce")
        df.dropna(subset=["TIME_PERIOD", "Osservazione"], inplace=True)

        # 3. Ordina per anno
        df = df.sort_values("TIME_PERIOD")

        # 4. Grafico ad area
        fig = px.area(
            df,
            x="TIME_PERIOD",
            y="Osservazione",
            color="DATA_TYPE",
            groupnorm=None,
            labels={
                "TIME_PERIOD": "Anno",
                "Osservazione": "Percentuale (%)",
                "DATA_TYPE": "Stato"
            },
            title="<b>Fumatori e Non fumatori 14–17 anni</b><br>Andamento nel tempo"
        )

        # 5. Layout
        fig.update_layout(
            font=dict(family="Arial", size=14),
            hovermode="x unified"
        )

        fig.show()

    except Exception as e:
        print(f"Errore: {e}")

generate_area_chart()