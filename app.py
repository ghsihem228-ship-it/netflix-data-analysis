import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Netflix Data Dashboard", layout="wide")

st.title("📊 Netflix Data Dashboard")
st.write("Interactive dashboard for exploring Netflix titles data.")

df = pd.read_csv("netflix_titles.csv")

df = df.dropna(subset=["type", "country", "release_year"])

st.sidebar.header("Filters")

type_filter = st.sidebar.selectbox(
    "Select Content Type",
    ["All"] + list(df["type"].unique())
)

min_year = int(df["release_year"].min())
max_year = int(df["release_year"].max())

year_range = st.sidebar.slider(
    "Select Year Range",
    min_year,
    max_year,
    (2000, max_year)
)

filtered_df = df[df["release_year"].between(year_range[0], year_range[1])]

if type_filter != "All":
    filtered_df = filtered_df[filtered_df["type"] == type_filter]

st.subheader("Dataset Preview")
st.dataframe(filtered_df.head(20))

col1, col2, col3 = st.columns(3)

col1.metric("Total Titles", len(filtered_df))
col2.metric("Movies", len(filtered_df[filtered_df["type"] == "Movie"]))
col3.metric("TV Shows", len(filtered_df[filtered_df["type"] == "TV Show"]))

st.subheader("Movies vs TV Shows")
type_counts = filtered_df["type"].value_counts()

fig1, ax1 = plt.subplots()
type_counts.plot(kind="bar", ax=ax1)
ax1.set_xlabel("Type")
ax1.set_ylabel("Count")
st.pyplot(fig1)

st.subheader("Top 10 Countries")
top_countries = filtered_df["country"].value_counts().head(10)

fig2, ax2 = plt.subplots()
top_countries.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Country")
ax2.set_ylabel("Count")
st.pyplot(fig2)

st.subheader("Content Growth Over Years")
year_counts = filtered_df["release_year"].value_counts().sort_index()

fig3, ax3 = plt.subplots()
year_counts.plot(ax=ax3)
ax3.set_xlabel("Year")
ax3.set_ylabel("Number of Titles")
st.pyplot(fig3)

st.success("Dashboard loaded successfully.")
