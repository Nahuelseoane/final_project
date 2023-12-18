import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def global_context(df: pd.DataFrame):
    sns.barplot(
        data=df,
        x="value",
        y="country_region",
        palette=df.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context");