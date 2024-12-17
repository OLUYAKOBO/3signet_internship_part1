import streamlit as st
import numpy as np
import pandas as pd
import pickle

st.set_page_config(page_title="Student Dropout Rate Prediction App", page_icon="📊", layout="wide")
st.title("*Student Dropout Rate Prediction App*")

#scaler = pickle.load(open('scal.pkl','rb'))
new_scaler = pickle.load(open('scal2.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.sidebar.markdown("""
    ### Key Features:
    - **Real-Time Student Dropout Prediction**: Instantly predicts the likelihood of a student graduating or dropping out based on their data.
    - **User-Friendly Interface**: Provides an intuitive web-based interface built with Streamlit for easy data input and feedback.
    - **Machine Learning Integration**: Utilizes advanced machine learning algorithms to ensure accurate and reliable predictions.
    - **Continuous Monitoring and Updates**: Regularly monitors performance and updates the model to maintain and enhance accuracy.
    """)

st.write(" ")
st.write(" ")
st.markdown("### Get Started!")
st.write('----')
st.markdown("*To get started, fill in your necessary Student details below;*")
st.write("")

def user_info():

    c1,c2 = st.columns(2)

    with c1:
        course = st.number_input('Enter your number of courses',33,10000,2344)
        prev_qua = st.number_input("Enter your previous qualification grade here",95,200,100)
        adm_grade = st.number_input("Enter your admission grade here",95,200,100)
        tuition = st.number_input("Enter your tuition fees status,(0 represents not paid, 1 represents fully paid)",0,1,1)
        curr1_ev = st.number_input("Enter your first semester evaluation units",0,45,20)

    with c2:
        curr1_app = st.number_input("Enter your first semester approved units",0,26,20)
        curr1_grade = st.number_input("Enter your first semester grade units",0,18,10)
        curr2_ev = st.number_input("Enter your second semester evaluation units",0,33,20)
        curr2_app = st.number_input("Enter your second semester approved units",0,20,10)
        curr2_grade = st.number_input("Enter your second semester grade units",0,19,10)


    feat = np.array([course,prev_qua,adm_grade,tuition,curr1_ev,curr1_app,curr1_grade,
                     curr2_ev,curr2_app,curr2_grade]).reshape(1,-1)
    
    cols = ['Course',
            'Previous qualification (grade)',
            'Admission grade',
            'Tuition fees up to date',
            'Curricular units 1st sem (evaluations)',
            'Curricular units 1st sem (approved)',
            'Curricular units 1st sem (grade)',
            'Curricular units 2nd sem (evaluations)',
            'Curricular units 2nd sem (approved)',
            'Curricular units 2nd sem (grade)']



    df = pd.DataFrame(feat, columns = cols)
    return df
df = user_info()


def scaling():
    df1 = df.copy()

    cols = df1.columns
    df1 = new_scaler.transform(df1)

    df1 = pd.DataFrame(df1, columns = cols)
    return df1
df1 = scaling()

prediction = model.predict(df1)
prediction_proba = model.predict_proba(df1)
approved_prob = np.round((prediction_proba[:, 1] * 100), 2)[0]

output = f"The probability that this student will graduate is {approved_prob}%"
#output2 = f"The probability that this student will dropout is {approved_prob}%"
import time
st.write("")
if st.button('*Click here to get your prediction*'):
    time.sleep(10)
    with st.spinner('Predicting... Please wait...'):
        if prediction == 0:
            st.success("This student will Drop out")
            st.write("")
            st.success(output)
        else:
            st.success("This student will Graduate")
            st.write("")
            st.success(output)
