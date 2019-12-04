import pandas as pd
from math import isnan
import os

def get_resource_dir():
    return os.path.dirname(os.path.abspath(__file__)) + os.path.sep + '..' + os.path.sep + 'resources' + os.path.sep

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
    if 'Monatsgehalt September'in df:
        for index, row in df.iterrows():
            print('Bonus für Mitarbeiter/in %s %s beträgt %s €' % (row.Vorname, row.Name, calculate_bonus(row['Monatsgehalt September'])))

# ------------------------------------------------------------------------------------------------------------------------------------ #

resource_dir_path = get_resource_dir()
gehaltsabrechnung_excel_path = resource_dir_path + 'Gehaltabrechnung.xlsx'
sheet_name = 'Tabelle1'

gehalt_df = read_excel_file(gehaltsabrechnung_excel_path, sheet_name)
print_result(gehalt_df[gehalt_df['Tarif'] == 'T1'])
