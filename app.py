import numpy as np
import pickle
import pandas as pd

import streamlit as st 

# from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"


def predict_note_authentication(Pclass,Age,SibSp,Parch,Fare,Male):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[Pclass,Age,SibSp,Parch,Fare,Male]])
    print(prediction)
    return prediction



def main():
    st.title("Tinanic Survival Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Titanic Survival Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    PassengerId = st.text_input("PassengerId")

    Name = st.text_input("Name")

    Pclass_options = {1,2,3}
    Pclass = st.selectbox("Pclass",list(Pclass_options))

    Age = st.text_input("Age")

    SibSp_opt = {0,1,2,2.5}
    SibSp = st.selectbox("SibSp",list(SibSp_opt))

    Parch_options = {0,1,2,3,4,5,6}
    Parch = st.selectbox("Parch",list(Parch_options))

    Fare = st.text_input("Fare")

    Cabin_options = {'T', 'Missing', 'A', 'G', 'C', 'F', 'B', 'E', 'D'}
    Cabin = st.selectbox("Cabin",list(Cabin_options))

    Sex_options = {"Female": 0, "Male": 1}
    Sex = st.selectbox("Sex", list(Sex_options.keys()))

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Pclass,Age,SibSp,Parch,Fare,Sex_options[Sex])
        if result:
            st.success('The person will survive')
        else :
            st.success("The person won't survive")
             
    # st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    