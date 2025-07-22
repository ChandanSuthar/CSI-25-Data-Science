import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans


st.title("Mall Customer Segmentation")

@st.cache_data
def load_data():
    df = pd.read_csv("Mall_Customers.csv")
    return df

data = load_data()

print("Data loaded. Number of rows:", data.shape[0])
print("Data loaded. Number of columns:", data.shape[1])

show_data = st.sidebar.checkbox("Show raw data")
if show_data:
    st.subheader("# Raw Data")
    st.dataframe(data.head(10))

st.subheader("# Exploratory Data Analysis")

st.write("### Gender Distribution")
gender_counts = data["Gender"].value_counts()
genders = gender_counts.index.tolist()
gender_values = gender_counts.values.tolist()

fig1, ax1 = plt.subplots(figsize=(6, 4))
ax1.bar(genders, gender_values)
ax1.set_xlabel("Gender")
ax1.set_ylabel("Number of Customers")
ax1.set_title("Count of Male vs Female")
plt.tight_layout()
st.pyplot(fig1)

st.write("### Age Distribution")
ages = data["Age"].tolist()
fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.hist(ages, bins=15, edgecolor='black')
ax2.set_xlabel("Age")
ax2.set_ylabel("Frequency")
ax2.set_title("Histogram of Customer Ages")
plt.tight_layout()
st.pyplot(fig2)

st.write("### Annual Income Distribution (in k$)")
incomes = data["Annual Income (k$)"].tolist()
fig3, ax3 = plt.subplots(figsize=(6, 4))
ax3.hist(incomes, bins=15, edgecolor='black')
ax3.set_xlabel("Annual Income (k$)")
ax3.set_ylabel("Frequency")
ax3.set_title("Histogram of Annual Incomes")
plt.tight_layout()
st.pyplot(fig3)

st.write("### Spending Score Distribution (1-100)")
scores = data["Spending Score (1-100)"].tolist()
fig4, ax4 = plt.subplots(figsize=(6, 4))
ax4.hist(scores, bins=15, edgecolor='black')
ax4.set_xlabel("Spending Score")
ax4.set_ylabel("Frequency")
ax4.set_title("Histogram of Spending Scores")
plt.tight_layout()
st.pyplot(fig4)

st.subheader("# Preprocessing")

df_copy = data.copy()

encoder = LabelEncoder()
df_copy["GenderEncoded"] = encoder.fit_transform(df_copy["Gender"])  

st.write("Encoded Gender column: Female → 0, Male → 1")
st.write(df_copy[["Gender", "GenderEncoded"]].head(5))

st.subheader("# Choose Number of Clusters (k)")

k = st.sidebar.slider(
    label="Select k (number of clusters)",
    min_value=2,
    max_value=10,
    value=5,
    step=1
)
st.write("You have selected k =", k)

st.subheader("# Prepare Data for Clustering")

feature_columns = ["GenderEncoded", "Age", "Annual Income (k$)", "Spending Score (1-100)"]
st.write("Features used:", feature_columns)

X = df_copy[feature_columns]

st.write("Shape of feature matrix X:", X.shape)

st.subheader("# Running KMeans")

kmeans_model = KMeans(n_clusters=k, random_state=42)

kmeans_model.fit(X)

cluster_labels = kmeans_model.labels_

df_copy["Cluster"] = cluster_labels

st.write("Clustering done. Here are the first 5 labeled rows:")
st.write(df_copy.head(5))

st.subheader("# Cluster Visualization")

fig5, ax5 = plt.subplots(figsize=(8, 6))
for cluster_num in range(k):

    cluster_data = df_copy[df_copy["Cluster"] == cluster_num]
    ax5.scatter(
        cluster_data["Annual Income (k$)"],
        cluster_data["Spending Score (1-100)"],
        label=f"Cluster {cluster_num}",
        s=40
    )

ax5.set_xlabel("Annual Income (k$)")
ax5.set_ylabel("Spending Score (1-100)")
ax5.set_title("Clusters: Income vs Spending Score")
ax5.legend(title="Cluster")
plt.tight_layout()
st.pyplot(fig5)

st.subheader("# Cluster Profiles")

cluster_means = df_copy.groupby("Cluster")[["Age", "Annual Income (k$)", "Spending Score (1-100)"]].mean()
cluster_counts = df_copy["Cluster"].value_counts().sort_index().rename("Count")

profile_table = pd.concat([cluster_counts, cluster_means], axis=1)

st.table(profile_table)

st.subheader("# How to Interpret Results")
st.write("- Identify clusters with high income but low spending score.")
st.write("- Identify clusters with low income but high spending score.")
st.write("- Note the average age in each cluster.")
st.write("- Use these findings to target marketing campaigns accordingly.")
