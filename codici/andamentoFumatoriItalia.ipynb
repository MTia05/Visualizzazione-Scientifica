import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv

# Carica il file
file_path = 'Tabella_1.csv'

try:
    # Gestione degli errori o problemi dovuti ai caratteri nel csv dell'ISTAT
    df = pd.read_csv(
        file_path,
        sep=',',
        encoding='latin-1',
        quoting=csv.QUOTE_NONE,
        on_bad_lines='skip'
    )

    # Pulizia delle colonne
    df.columns = [c.strip().replace('"', '').replace("'", "") for c in df.columns]

    # Indici colonne: 10 - Anno, 11 - Valore in migliaia
    col_anno_idx = 10
    col_valore_idx = 11

    # Creazione del frame di lavoro
    data = pd.DataFrame({
        'Anno': df.iloc[:, col_anno_idx],
        'Fumatori': df.iloc[:, col_valore_idx]
    })

    # Conversione
    data['Anno'] = pd.to_numeric(data['Anno'], errors='coerce')
    data['Fumatori'] = pd.to_numeric(data['Fumatori'], errors='coerce')
    data = data.dropna().sort_values(by='Anno')

    # Converte i fumatori da migliaia a milioni
    data['Fumatori'] = data['Fumatori'] / 1000

    # Configurazione grafica
    sns.set_theme(style="white")
    fig, ax = plt.subplots(figsize=(14, 8), dpi=100)

    # Colori
    sky_blue = '#5DADE2'  # Blu Cielo
    text_color = '#2E4053' # Colore per il titolo principale
    sub_color = '#95A5A6'  # Colore per gli assi

    # Disegno della linea
    plt.plot(
        data['Anno'],
        data['Fumatori'],
        color=sky_blue,
        linewidth=2.5,
        marker='o',
        markersize=6,
        markerfacecolor=sky_blue,
        markeredgecolor=sky_blue,
        zorder=3
    )

    # Valori sopra ogni pallino in milioni
    for x, y in zip(data['Anno'], data['Fumatori']):
        ax.annotate(
            f'{y:.2f}M',
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha='center',
            fontsize=9,
            fontweight='bold',
            color=text_color
        )

    # Titolo principale
    plt.title('Andamento Fumatori in Italia',
              fontsize=22, pad=50, fontweight='bold', color=text_color, loc='left')

    # Sottotitolo
    ax.text(0, 1.06, 'Persone dai 14 anni in su • Valori in milioni',
            transform=ax.transAxes,
            fontsize=12,
            color=sub_color,
            fontweight='normal')

    # Nomi degli assi
    plt.xlabel('Anno di rilevazione', fontsize=11, labelpad=15, color=sub_color)
    plt.ylabel('Fumatori (milioni)', fontsize=11, labelpad=15, color=sub_color)

    # Rimuove i bordi
    sns.despine(left=True, bottom=True)

    # Griglia orizzontale si verticale no
    ax.yaxis.grid(True, linestyle='-', alpha=0.1, color='black')
    ax.xaxis.grid(False)

    # Valori degli assi
    plt.xticks(data['Anno'].unique().astype(int), rotation=45, fontsize=10, color=sub_color)
    plt.yticks(fontsize=10, color=sub_color)

    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Errore durante l'elaborazione: {e}")
