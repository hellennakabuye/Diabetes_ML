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
        return 'This person is Non-diabetic'
    else:
        return 'This person is Diabetic'


def main():

    # giving title
    st.title('Diabetes Prediction App')
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


if __name__ == '__main__':
    main()
