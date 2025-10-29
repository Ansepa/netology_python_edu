python
import pandas as pd
df = pd.read_csv("data.csv",nrows=15)

df["age_category"] = df["age"].apply(lambda x: "Старше 25" if x > 25 else "Младше или равен 25")

print(df["age_category"])
