import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv",nrows=15)

filtered_df = df[(df["sex"] == "male") & (df["age"] > 30)]
pd.set_option('display.max_columns', None)

print(filtered_df)

pd.set_option('display.max_columns', None)

fig, ax = plt.subplots(figsize=(12, 4))
ax.axis('off')
table = ax.table(cellText=filtered_df.values, colLabels=filtered_df.columns, loc='center')
plt.savefig("table.png", bbox_inches='tight', dpi=200)
