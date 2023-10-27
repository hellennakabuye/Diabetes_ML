import pickle
import streamlit
import numpy as np

# loading saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

input_data = (5,116,74,0,0,25.6,0.201,30)

# changing input data to a numpy array
inputdataasnumpyarray = np.asarray(input_data)

#reshape the array)
input_data_reshaped = inputdataasnumpyarray.reshape(1, -1)

# MAKE PREDICTION
prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if prediction == 0:
  print('This person is Non-diabetic')
else:
  print('This person is Diabetic')