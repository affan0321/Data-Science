import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="Set2")

fig, ax = plt.subplots()
sns.lineplot(x=[1,2,3,4], y=[10,15,7,20], marker="o", ax=ax)

ax.set_title("Monthly Sales", fontsize=16, fontweight="bold")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")

st.pyplot(fig)