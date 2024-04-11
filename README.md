# Leistungsdiagnostik Vorgehen Setup:

1. In VS-Code Dateien erstellen:
    - activity.csv -> ist die Angabe
    - sort.py -> für den späteren Bubble-Sort-Alhorithmus
    - load_data.py -> um die Daten im Format csv in eine Liste umzuschreiben

2. Virtuelle Umgebung aktivieren, um sicherzustellen, dass die Bedingungen in der Zukunft die selben sind wie aktuell und der Code funktioniert (z.B.: dass sich numpy nicht updated und wir somit unnötige Fehler vermeiden)
    - Virtuelle Umgebung aktivieren mittels /venv
    - in Kommandozeile: <Umgebungsname>\Scripts\activate
    - falls Probleme auftreten: Set-ExecutionPolicy -ExecutionPolicy Unrestricted (hat Sicherheitsgründe)

2. Code erstellen, um die Daten aus dem activity.csv in eine Liste umzuwandeln

3. Mittels Bubble-Sort die Liste sortieren

4. Code erstellen, um die Daten der Liste von load_data.py in einem Plot zu plotten

5. Plot als .png speichern

# Nice-to-know:

- **.venv\Scripts\activate**: es wird nicht auf die vorinstallierte Version zugegriffen, sondern neu in der virtuellen Ebene erstellt

- **pip numpy/matplotlib**: so werden Bibliotheken in der ordnerspeziefischen virtuellen Ebene installiert (Powershell Ebene als ADMINISTRATOR ÖFFNEN!!!)

- **python .\load_data.py**: öffnet die Daten aus einem anderen File in neuem File (Datenverschiebung)

- **pip freeze**: aktueller Zustand von den Bibliotheken (Versionen) werden angezeigt/eingefrohren -> stellt somit sicher, dass der Code auf allen PCs die selben Startbedingungen hat

