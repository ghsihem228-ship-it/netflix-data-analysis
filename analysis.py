import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")

# Clean data
df = df.dropna(subset=["type", "country", "release_year"])

# Movies vs TV Shows
type_counts = df["type"].value_counts()
print(type_counts)

type_counts.plot(kind="bar", title="Movies vs TV Shows")
plt.show()

# Top countries
top_countries = df["country"].value_counts().head(10)

top_countries.plot(kind="bar", title="Top Countries")
plt.show()
