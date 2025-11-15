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

missing = data.isna().sum()
print(missing)


clean = data.copy()
categorical_cols = ["pain", "peristalsis", "abdominal_distension", "outcome"]
numeric_cols = ["rectal_temp", "pulse", "respiratory_rate", "packed_cell_volume"]
for col in numeric_cols:
    clean[col] = clean[col].fillna(clean[col].median())


for col in categorical_cols:
    if col != "outcome":
        clean[col] = clean[col].fillna(clean[col].mode()[0])

clean = clean.dropna(subset=["outcome"])
