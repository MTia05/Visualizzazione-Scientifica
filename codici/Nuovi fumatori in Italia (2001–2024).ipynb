import plotly.graph_objects as go
import pandas as pd
import os

file_name = "/content/drive/MyDrive/Visualizzazione/Fumatorinuovi2001-2024_radar.csv"

def generate_radar_chart():

    if not os.path.exists(file_name):
        print(f"ERRORE: Il file '{file_name}' non è stato trovato.")
        return

    try:
        df = pd.read_csv(file_name)

        # Conversione colonne
        df["TIME_PERIOD"] = pd.to_numeric(df["TIME_PERIOD"], errors="coerce")
        df["Osservazione"] = pd.to_numeric(df["Osservazione"], errors="coerce")
        df.dropna(subset=["TIME_PERIOD", "Osservazione"], inplace=True)

        # Ordina per anno
        df = df.sort_values("TIME_PERIOD")

        # Dati radar
        years = df["TIME_PERIOD"].astype(int).astype(str).tolist()
        values = df["Osservazione"].tolist()

        # chiusura poligono
        years.append(years[0])
        values.append(values[0])

        # Grafico radar
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=years,
            fill="toself",
            line=dict(width=3)
        ))

        fig.update_layout(
            title="<b>Nuovi fumatori in Italia (2001–2024)</b><br>Numero assoluto",
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(values) * 1.15]
                )
            ),
            font=dict(family="Arial", size=14),
            showlegend=False
        )

        fig.show()

    except Exception as e:
        print(f"Errore: {e}")

generate_radar_chart()