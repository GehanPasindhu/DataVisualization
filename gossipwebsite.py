import json
import streamlit as st

# Load JSON data
with open("data.json", "r") as f:
    websites_list = json.load(f)

st.title("Gossip Websites")

# Create a table to display the data
st.table(websites_list)
