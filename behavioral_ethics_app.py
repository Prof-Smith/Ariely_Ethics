
import streamlit as st
import pandas as pd
import os

# File to store responses
DATA_FILE = "responses.csv"

# Load existing data
if os.path.exists(DATA_FILE):
    df = pd.read_csv(DATA_FILE)
else:
    df = pd.DataFrame(columns=["Reflection", "Debate Opinion"])

# Sidebar navigation
st.sidebar.title("Activity Navigation")
st.sidebar.markdown("""
- Activity Overview
- Learning Objectives
- Materials Needed
- Case Study Review
- Class Debate
- Reflection
- Extension Ideas
""")

# Main content
st.title("The Ethics of Behavioral Research: A Case Study of Dan Ariely")

st.header("Activity Overview")
st.markdown("""
This classroom activity explores the ethical dimensions of behavioral economics research using the controversy surrounding Dan Ariely's work as a case study.
""")

st.header("Learning Objectives")
st.markdown("""
- Understand the importance of data integrity and replication in behavioral economics.
- Analyze the ethical dimensions of academic research.
- Evaluate the impact of flawed research on public policy and pedagogy.
""")

st.header("Materials Needed")
st.markdown("""
- Copies of the retracted Ariely paper (or excerpts)
- Blog post from Data Colada analyzing the data
- Summary of Duke University's investigation (if available)
- Whiteboard or digital collaboration tool
- Optional: short video clip of Ariely discussing ethics or dishonesty
""")

st.header("Case Study Review")
st.markdown("""
In small groups, analyze the Ariely case and answer:
- What went wrong?
- Who is responsible?
- How could this have been prevented?
""")

st.header("Class Debate")
debate_opinion = st.radio("What is your opinion?", [
    "Yes, it should be taught for its historical and cautionary value",
    "No, it should be removed due to ethical concerns",
    "It should be taught with critical context and disclaimers"
])

st.header("Reflection")
reflection = st.text_area("What will you do differently when evaluating behavioral research in the future?")

if st.button("Submit Response"):
    new_entry = pd.DataFrame([[reflection, debate_opinion]], columns=["Reflection", "Debate Opinion"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    st.success("Your response has been recorded!")

st.header("Poll Results")
if not df.empty:
    st.bar_chart(df["Debate Opinion"].value_counts())

st.header("Extension Ideas")
st.markdown("""
- Replicate a simple behavioral study using open data.
- Introduce tools like pre-registration platforms.
- Invite a guest speaker on research ethics or meta-science.
""")
