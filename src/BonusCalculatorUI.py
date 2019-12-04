import tkinter as tk
from math import isnan
from tkinter import filedialog

import pandas as pd

work_sheet_name = "Tabelle1"

def read_excel_file(excel_file_path, sheet_name):
    return pd.read_excel (excel_file_path, sheet_name)

def calculate_bonus(salary):
    return '{:.2f}'.format(convert_salary_to_number(salary) * 0.02 + 100).replace('.', ',')

def convert_salary_to_number(salary):
    if not isinstance(salary, int) and not isinstance(salary, float):
        try:
            return float(salary)
        except ValueError:
            return 0

    if isnan(salary):
        return 0

    return salary

def get_result(df):
    result = []

    if 'Monatsgehalt September'in df:
        for index, row in df.iterrows():
            result.append('Bonus für Mitarbeiter/in %s %s beträgt %s €' % (row.Vorname, row.Name, calculate_bonus(row['Monatsgehalt September'])))

    return result

def get_excel():
    import_file_path = filedialog.askopenfilename()
    df = read_excel_file(import_file_path, work_sheet_name)
    create_result_window(get_result(df[df['Tarif'] == 'T1']))

def create_result_window(results):
    result_window = tk.Toplevel()
    result_window.wm_title('Ergebnis')
    result_window.configure(background='lightsteelblue')

    if len(results) == 0:
        result_row = tk.Label(result_window, text="Keine Ergebnisse", fg='black', bg='lightsteelblue', font = ('helvetica', 8, 'bold'))
        result_row.pack(side="top", fill="both", expand=True, padx=10, pady=10)
    else:
        for result in results:
            result_row = tk.Label(result_window, text=result, fg='black', bg='lightsteelblue', font = ('helvetica', 8, 'bold'))
            result_row.pack(side="top", fill="both", expand=True, padx=5, pady=5)

    button1 = tk.Button(result_window, text='Schließen', command = close_windows, bg = 'green', fg = 'white', font = ('helvetica', 12, 'bold'))
    button1.pack(side='bottom')

def close_windows():
    root.destroy()

def create_main_window():
    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
    canvas1.pack()

    browse_button_excel = tk.Button(text = 'Import Excel File', command = get_excel, bg = 'green', fg = 'white', font = ('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=browse_button_excel)

    root.mainloop()

# ---------------------------------------------------- Main part ------------------------------------------------------------------------------- #

root = tk.Tk()
root.title('Bonus Calculator')
create_main_window()