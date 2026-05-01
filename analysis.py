
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# -----------------------
# Data Cleaning
# -----------------------
df = df.dropna(subset=["type", "country", "release_year"])

# -----------------------
# Movies vs TV Shows
# -----------------------
type_counts = df["type"].value_counts()
print("\nMovies vs TV Shows:\n", type_counts)

plt.figure()
type_counts.plot(kind="bar", title="Movies vs TV Shows", color=["blue", "orange"])
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("movies_vs_tv.png")
plt.close()

# -----------------------
# Top Countries
# -----------------------
top_countries = df["country"].value_counts().head(10)
print("\nTop Countries:\n", top_countries)

plt.figure()
top_countries.plot(kind="bar", title="Top 10 Countries", color="green")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("top_countries.png")
plt.close()

# -----------------------
# Content Over Years
# -----------------------
year_counts = df["release_year"].value_counts().sort_index()

plt.figure()
year_counts.plot(title="Content Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_over_years.png")
plt.close()

print("\nAnalysis completed. Charts saved.")
