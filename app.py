import streamlit as st
import numpy as np
import joblib

model = joblib.load('svm_model.pkl')

st.set_page_config(
    page_title="Titanic Survival Prediction",
    page_icon="🚢",
    layout="centered"
)

st.sidebar.header("🧍 Passenger Details")

pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
Age = st.sidebar.number_input("Age", min_value=0, max_value=100, value=25)
Fare = st.sidebar.number_input("Fare Price", min_value=0, max_value=600, value=50)
sex = st.sidebar.selectbox("Gender", ["male", "female"])
Embarked = st.sidebar.selectbox("Port of Embarkation", ["S", "C", "Q"])
Family_size = st.sidebar.number_input(
    "Family Size (Alone = 1)", min_value=1, max_value=20, value=1
)
sex_numeric= 1 if sex =='male' else 0
Embarked_S=0
Embarked_C=0
Embarked_Q=0
match Embarked:
    case 'S':
        Embarked_S=1
    case 'C':
        Embarked_C=1
    case 'Q':
        Embarked_Q=1

st.title("🚢 Titanic Survival Prediction")
st.markdown(
    """
    This app uses a **Machine Learning SVM model**  
    to predict whether a passenger **survived** the Titanic disaster.
    """
)
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.metric("Passenger Class", pclass)
    st.metric("Age", Age)

with col2:
    st.metric("Fare", Fare)
    st.metric("Family Size", Family_size)

X_input=np.array([pclass,Age,Fare,sex_numeric,Embarked_S,Embarked_C,Embarked_Q,Family_size]).reshape(1,-1)

if st.button("🔮 Predict Survival", use_container_width=True):
    with st.spinner("Predicting..."):
        pred = model.predict(X_input)

    st.divider()

    if pred[0] == 1:
        st.success("🟢 **Survived** — High chance of survival!")
        st.balloons()
    else:
        st.error("🔴 **Did Not Survive** — Low chance of survival.")

with st.expander("ℹ️ Feature Explanation"):
    st.markdown("""
    - **Passenger Class**: 1st, 2nd, or 3rd class  
    - **Fare**: Ticket price paid  
    - **Family Size**: Number of relatives onboard  
    - **Embarked**: Port where passenger boarded  
    - **Sex**: Male or Female
    """)

st.markdown("""
<style>
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        height: 3em;
        font-size: 18px;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)
