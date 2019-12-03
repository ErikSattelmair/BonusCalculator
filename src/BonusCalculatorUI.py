import tkinter as tk
from tkinter import filedialog
import pandas as pd
from math import isnan

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

def print_result(df):
    for index, row in df.iterrows():
        print('Bonus für Mitarbeiter/in %s %s beträgt %s €' % (row.Vorname, row.Name, calculate_bonus(row['Monatsgehalt September'])))

def get_excel ():
    global df

    import_file_path = filedialog.askopenfilename()
    df = read_excel_file(import_file_path, work_sheet_name)
    print_result(df[df['Tarif'] == 'T1'])
    root.destroy()

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

browseButton_excel = tk.Button(text = 'Import Excel File', command = get_excel, bg = 'green', fg = 'white', font = ('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_excel)

root.mainloop()