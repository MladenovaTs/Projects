# Libraries
import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load the trained model
model = joblib.load('Mladenova_Data_Scientist_Project1_ridge_regression_model.pkl')

# Title
st.title('Automobile Price Prediction')

# Dropdown for 'Car Brand'
make_options = ['<Please select>',
                'alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda', 'isuzu', 'jaguar', 'mazda',
                'mercedes-benz', 'mercury', 'mitsubishi', 'nissan', 'peugot', 'plymouth', 'porsche',
                'renault', 'saab', 'subaru', 'toyota', 'volkswagen', 'volvo']
make = st.selectbox('Car Brand', make_options)

# Dropdown for 'Aspiration'
aspiration_options = ['<Please select>', 'std', 'turbo']
aspiration = st.selectbox('Aspiration', aspiration_options)

# Slider for 'Horsepower'
horsepower = st.slider('Horsepower', min_value=48, max_value=262)

# Slider for 'Curb Weight'
curb_weight = st.slider('Curb Weight', min_value=1488, max_value=4066)

# Calculate power_weight_ratio based on user inputs
power_weight_ratio = horsepower / curb_weight

# Predict price function
def predict_price():
    # Prepare input data
    input_data = {'make': make, 'aspiration': aspiration, 'power_weight_ratio': power_weight_ratio}
    input_df = pd.DataFrame([input_data])

    # One-hot encode 'make' and 'aspiration'
    input_df = pd.get_dummies(input_df, columns=['make', 'aspiration'])
    input_features = input_df.columns

    # Prepare model input
    model_input = np.zeros(len(model.coef_))
    for feature in input_features:
        if feature in model.coef_:
            model_input[input_features.get_loc(feature)] = input_df[feature].values[0]

    # Predict price
    predicted_price = model.predict([model_input])
    st.write(f'Predicted Price: ${predicted_price[0]:.2f}')

# Button to predict price
if st.button('Predict Price'):
    predict_price()












# # Function to predict price when the button is clicked
# def predict_price():
#     # Prepare input data for prediction
#     input_data = {
#         'make': make,
#         'aspiration': aspiration,
#         'power_weight_ratio': power_weight_ratio
#     }
#     print("Input Data:", input_data)

#     # Create a DataFrame from the input data
#     input_df = pd.DataFrame([input_data])
#     print("Input DataFrame:")
#     print(input_df)

#     # One-hot encode 'make' and 'aspiration' variables
#     input_df = pd.get_dummies(input_df, columns=['make', 'aspiration'])
#     print("One-hot Encoded DataFrame:")
#     print(input_df)

#     # Get the column names after one-hot encoding
#     input_features = input_df.columns
#     print("Input Features:", input_features)

#     # Initialize an empty list to store feature names
#     model_features = []

#     # Iterate over the input features and check if they are present in the model coefficients
#     for feature in input_features:
#         if feature in model.coef_:
#             model_features.append(feature)
#     print("Model Features:", model_features)

#     # Initialize an array of zeros with the same size as the number of features expected by the model
#     model_input = np.zeros(len(model.coef_))
#     print("Model Input (before filling with user input):", model_input)

#     # Fill the array with the values provided by the user
#     for feature in model_features:
#         model_input[model_features.index(feature)] = input_df[feature].values[0]
#     print("Model Input (after filling with user input):", model_input)

#     # Predict the price using the modified input
#     predicted_price = model.predict([model_input])
#     print("Predicted Price:", predicted_price)

#     # Display Prediction
#     st.write(f'Predicted Price: ${predicted_price[0]:.2f}')








# import streamlit as st
# import joblib
# import pandas as pd
# import numpy as np

# # Load the trained model
# model = joblib.load('ridge_regression_model.pkl')

# # Title
# st.title('Automobile Price Prediction')

# # Dropdown list for 'Car Make' input
# make_options = ['<Please select>', 'alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda', 'isuzu', 'jaguar', 'mazda', 'mercedes-benz', 'mercury', 'mitsubishi', 'nissan', 'peugot', 'plymouth', 'porsche', 'renault', 'saab', 'subaru', 'toyota', 'volkswagen', 'volvo']
# make = st.selectbox('Car Make', make_options)

# # Input field for 'Aspiration'
# aspiration_options = ['<Please select>', 'std', 'turbo']
# aspiration = st.selectbox('Aspiration', aspiration_options)

# # Slider for 'Horsepower'
# horsepower = st.slider('Horsepower', min_value=48, max_value=262)

# # Slider for 'Curb Weight'
# curb_weight = st.slider('Curb Weight', min_value=1488, max_value=4066)

# # Calculate power_weight_ratio based on user inputs
# power_weight_ratio = horsepower / curb_weight

# # Function to predict price when the button is clicked
# def predict_price():
#     print("Starting prediction function...")
#     # Prepare input data for prediction
#     input_data = {
#         'make': make,
#         'aspiration': aspiration,
#         'power_weight_ratio': power_weight_ratio
#     }
#     print("Input data:", input_data)

#     # Create a DataFrame from the input data
#     input_df = pd.DataFrame([input_data])
#     print("Input DataFrame:")
#     print(input_df)

#     # One-hot encode 'make' and 'aspiration' variables
#     input_df = pd.get_dummies(input_df, columns=['make', 'aspiration'])
#     print("One-hot encoded DataFrame:")
#     print(input_df)

#     # Get the column names after one-hot encoding
#     input_features = input_df.columns
#     print("Input features:", input_features)

#     # Initialize an empty list to store feature names
#     model_features = []

#     # Iterate over the input features and check if they are present in the model coefficients
#     for feature in input_features:
#         if feature in model.coef_:
#             model_features.append(feature)
#     print("Model features used for prediction:", model_features)

#     # Initialize an array of zeros with the same size as the number of features expected by the model
#     model_input = np.zeros(len(model.coef_))
#     print("Model input array before filling with values:", model_input)

#     # Fill the array with the values provided by the user
#     for feature in model_features:
#         model_input[model_features.index(feature)] = input_df[feature].values[0]

#     print("Model input array after filling with values:", model_input)

#     # Predict the price using the modified input
#     predicted_price = model.predict([model_input])

#     # Display Prediction
#     st.write(f'Predicted Price: ${predicted_price[0]:.2f}')
#     print("Predicted Price:", predicted_price)

# # Button to predict price
# if st.button('Predict Price'):
#     print("Predict button clicked.")
#     predict_price()










































