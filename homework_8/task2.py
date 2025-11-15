import ssl
import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/obulygin/pyda_homeworks/master/statistics_basics/horse_data.csv"

column_names = [
    "surgery","age","hospital_number","rectal_temp","pulse","respiratory_rate",
    "temp_extremities","peripheral_pulse","mucous_membranes","capillary_refill",
    "pain","peristalsis","abdominal_distension","nasogastric_tube",
    "nasogastric_reflux","nasogastric_reflux_ph","rectal_exam_feces",
    "abdomen","packed_cell_volume","total_protein","abdom_appearance",
    "abdom_total_protein","outcome","surgical_lesion","lesion_1","lesion_2",
    "lesion_3","cp_data"
]

df = pd.read_csv(url, header=None, names=column_names, na_values='?')

cols = [
    "rectal_temp",
    "pulse",
    "respiratory_rate",
    "packed_cell_volume",
    "pain",
    "peristalsis",
    "abdominal_distension",
    "outcome"
]

data = df[cols]
data.head()



def find_outliers(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    low = Q1 - 1.5 * IQR
    high = Q3 + 1.5 * IQR
    outliers = series[(series < low) | (series > high)]
    return outliers, low, high

outliers_dict = {}
numeric_cols = ["rectal_temp", "pulse", "respiratory_rate", "packed_cell_volume"]

for col in numeric_cols:
    outliers, low, high = find_outliers(data[col].dropna())
    outliers_dict[col] = len(outliers)
    print(f"{col}: выбросов = {len(outliers)}, границы [{low:.2f}, {high:.2f}]")
