import pandas as pd
import seaborn  as sns
import matplotlib.pyplot as plt
df = pd.read_csv("data.csv",nrows=15)

sns.scatterplot(data=df,x="age",y="bill")
plt.title("Зависимость суммы счёта от возраста клиента")
plt.xlabel("Возраст клиента")
plt.ylabel("Сумма счёта")
plt.show()
