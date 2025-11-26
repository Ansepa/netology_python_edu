import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score




def analyze_group(df, name):
    print(f"\n{name}:")

    # График
    sns.scatterplot(data=df, x='hardness', y='mortality')
    plt.title(f'Жёсткость воды vs. Смертность ({name})')
    plt.show()

    # Корреляции
    pearson_corr, pearson_p = pearsonr(df['hardness'], df['mortality'])
    spearman_corr, spearman_p = spearmanr(df['hardness'], df['mortality'])
    print(f"Пирсон: {pearson_corr:.3f}, p-value: {pearson_p:.3f}")
    print(f"Спирмен: {spearman_corr:.3f}, p-value: {spearman_p:.3f}")

    # Линейная регрессия
    X = df[['hardness']]
    y = df['mortality']
    model = LinearRegression().fit(X, y)
    y_pred = model.predict(X)
    print(f"Регрессия: slope={model.coef_[0]:.3f}, intercept={model.intercept_:.3f}")

    # R^2
    r2 = r2_score(y, y_pred)
    print(f"R^2: {r2:.3f}")

    # Остатки
    residuals = y - y_pred
    plt.scatter(y_pred, residuals)
    plt.axhline(0, color='red', linestyle='--')
    plt.title(f'График остатков ({name})')
    plt.show()

df = pd.read_csv("water.csv")
north = df[df['location'] == 'North']
south = df[df['location'] == 'South']
analyze_group(df, "Все города")
analyze_group(north, "Северные города")
analyze_group(south, "Южные города")
