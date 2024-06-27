import numpy as np
import pickle
import streamlit as st

# loading saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))


# function for prediction
def diabetes_prediction(input_data):

    # changing input data to a numpy array
    inputdataasnumpyarray = np.asarray(input_data)

    # reshape the array)
    input_data_reshaped = inputdataasnumpyarray.reshape(1, -1)

    # MAKE PREDICTION
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction == 0:
        return 'This person is predicted Non-diabetic'
    else:
        return 'This person is predicted Diabetic'


def main():

    # giving title
    st.title('Diabetes Prediction App')
    with st.sidebar:
        st.sidebar.title(':blue[Welcome to ***diabetes_ai***]')
        st.header("About Diabetes")
        st.write("Types: Type 1, Type 2 & Gestational Diabetes")
        st.write("Symptoms: Chronic thirst, frequent urinating, sudden weight loss, irritability, blurry vision & more")
        st.write("Risk factors: Family history, race or ethnicity, body weight & more")
        st.write("Source: www.mayoclinic.org")
        st.header("Developer: Hellen Nakabuye")
        st.write("Email: hellennakabuye23@gmail.com")
        st.write("Phone: +256703145793")
        st.write("Data source: www.kaggle.com")


    # getting input data from user
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose Levels')
    BloodPressure = st.text_input('Blood pressure value')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age')

    # Code for prediction
    diagnosis = ''
    # button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

    st.success(diagnosis)
    st.header(':blue[Thank you for using ***diabetes_ai***]')


if __name__ == '__main__':
    main()
