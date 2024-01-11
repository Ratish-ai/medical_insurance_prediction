import streamlit as st
from pred import *

st.title("Health Insurance Cost Prediction")
st.subheader("Enter your details")
age = st.number_input("Enter your age",min_value = 18,max_value = 70,step=1)
col1,col2 = st.columns(2)
with col1:
    diab = st.selectbox(
        "Do you have Diabetics",
        (
            "No",
            "Yes"
        )
    )
    if diab=="Yes":
        diab = 1
    else:
        diab = 0
with col2:
    bp = st.selectbox(
        "Do you have abnormal BP",
        (
            "No",
            "Yes"
        )
    )
    if bp=="Yes":
        bp = 1
    else:
        bp = 0

col1,col2 = st.columns(2)
with col1:
    trans = st.selectbox(
        "Have you ever done any Transplant before",
        (
            "No",
            "Yes"
        )
    )
    if trans=="Yes":
        trans = 1
    else:
        trans = 0
with col2:
    dis = st.selectbox(
        "Do you have any Chronical disease like Asthma, etc.",
        (
            "No",
            "Yes"
        )
    )
    if dis=="Yes":
        dis = 1
    else:
        dis = 0

col1,col2 = st.columns(2)
with col1:
    height = st.number_input("Enter your Height in metres",min_value=140,max_value=220)
with col2:
    weight = st.number_input("Enter your weight in KG",min_value=45,max_value=140)

col1,col2 = st.columns(2)
with col1:
    aller = st.selectbox(
        "Do you have any allergies",
        (
            "No",
            "Yes"
        )
    )
    if aller=="Yes":
        aller = 1
    else:
        aller = 0
with col2:
    cancer = st.selectbox(
        "Have your any of the family member got with any type of cancer",
        (
            "No",
            "Yes"
        )
    )
    if cancer=="Yes":
        cancer = 1
    else:
        cancer = 0

maj_sur = st.selectbox(
        "Have you ever done a major surgery",
        (
            "No",
            "Yes"
        )
    )
if maj_sur=="Yes":
    maj_sur = 1
else:
    maj_sur = 0
if st.button("Predict !!!"):
    st.subheader("Predicted value")