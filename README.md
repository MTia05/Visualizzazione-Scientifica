# L'Invisibile Visibile
### Visualizzazione Scientifica

*Università degli Studi di Milano - Corso di Laurea in Informatica - a.a. 2025/2026*

---

## Gruppo di Lavoro
* **Curia Matteo** - Matricola [51493A]
* **Di Febo Leonardo** - Matricola [48514A]
* **Ginex Mattia** - Matricola [62248A]
* **Guzzi Giuseppe** - Matricola [63238A]

---

## Obiettivo del Progetto
"L'Invisibile Visibile" esplora la capacità della visualizzazione scientifica di estrarre significato da dataset complessi, trasformando righe di dati grezzi in rappresentazioni visive intuitive e scientificamente rigorose.

Il progetto si è concentrato sull'analisi dei dati riguardanti il vizio del fumo, cercando di evidenziare pattern e correlazioni non immediatamente visibili nei dati tabulari.

---

## Struttura della Repository
La repository è organizzata come segue per facilitare la navigazione e la riproducibilità dei risultati:

* **[`codici/`](./codici/)**: Notebook Jupyter (formato `.ipynb` di Google Colab) contenenti la pipeline di elaborazione, pulizia e generazione dei grafici.
* **[`dataSet/`](./dataSet/)**: Tutti i file di input in formato `.csv` utilizzati per le analisi.
* **[`grafici/`](./grafici/)**: Raccolta dei risultati finali esportati (plot statici).
* **[Presentazione PDF](VisualizzazioneScientifica.pdf)**: Documentazione completa del lavoro svolto.
---

## Tecnologie Utilizzate
Per lo sviluppo della pipeline di visualizzazione abbiamo adottato l'ecosistema Python:
* **Google Colab** come ambiente di sviluppo collaborativo.
* **Pandas** per la manipolazione e l'analisi dei dati nei file CSV.
* **Matplotlib / Seaborn / Plotly** per la generazione dei grafici scientifici.

---

## Metodologia e Risultati
L'analisi è stata suddivisa in diverse fasi, ognuna documentata all'interno dei notebook nella cartella `codici`:
1.  **Preprocessing**: Pulizia dei dati e gestione dei valori mancanti presenti nei file originali.
2.  **Mappatura Visiva**: Scelta delle variabili visive (colori, assi, scale) per rappresentare al meglio le dimensioni del dataset.
3.  **Visualizzazione**: Generazione di grafici che permettono di osservare i dati a colpo d'occhio.

> Potete visualizzare tutti i render finali nella cartella `grafici/`.

---

## Come Eseguire i Notebook
1.  Accedere alla cartella `codici/`.
2.  Aprire i file `.ipynb` tramite **Google Colab**.
3.  Assicurarsi di caricare i file necessari dalla cartella `dataSet/`.
