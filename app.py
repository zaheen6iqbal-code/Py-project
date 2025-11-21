import streamlit as st
import pickle 


## to load the model and label encoder
## rb = run binary
model = pickle.load(open("car_model.pkl","rb"))
le = pickle.load(open("label_encoder.pkl","rb"))

st.title("Car Price Prediction app")

#dropdown for car model (from labelencoder classes)

car_model = st.selectbox("Select Car Model", le.classes_)

#user input

mileage = st.number_input("Enter Mileage (in miles)", min_value=0)
age = st.slider("Car age (year)",0,8)

## selected car model to encode value for prediction

encoded_model = le.transform([car_model])[0]

if st.button("Predict Price"):
    input_data = [[encoded_model,mileage,age]]
    predicted_price = model.predict(input_data)
    st.success(f"Estimated selling price: {predicted_price[0]}")
    
st.success(f"Zaheen Iqbal Khan")





