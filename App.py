# import statements
import streamlit as st

# Title of the page
st.title("Unit Converter")

# Conversion Units
conversion_types = ["Length","Weight","Temperature"]

# User Input Choises
conversion_choice = st.selectbox("Choose Conversion Types : ", conversion_types)

# Length Conversion

if conversion_choice == "Length":
    length_units = ["Centimeters","Meters","Kilometers","Inches","Feet"]
    input_value = st.number_input("Enter Length Value", min_value=0.0, format="%.3f")
    from_unit = st.selectbox("From Unit: ",length_units)
    to_unit = st.selectbox("To Unit: ",length_units)

    # Evaluation Dictionaries

    length_conversion = {
        "Centimeters": 0.01,
        "Meters": 1,
        "Kilometers": 1000,
        "Inches": 0.0254,
        "Feet": 0.3048
    }

    # Conversion Logic

    if st.button("Convert"):
        result = input_value * length_conversion[from_unit] / length_conversion[to_unit]
        st.success(f"{input_value} {from_unit} = {result:.2f} {to_unit}")

# Weight Conversion

elif conversion_choice == "Weight":
    weight_units = ["Kilograms","Grams","Pounds","Ounces"]
    input_value = st.number_input("Enter Weight Value", min_value= 0.0, format="%.2f")
    from_unit = st.selectbox("From Unit: ", weight_units)
    to_unit = st.selectbox("To Unit: ",weight_units)
    
    # conversion dictionaries

    weight_conversion = {
        "Kilograms": 1,
        "Grams": 0.001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    }

    # conversion logic

    if st.button("Convert"):
        result = input_value * weight_conversion[from_unit] / weight_conversion[to_unit]
        st.success(f"{input_value} {from_unit} = {result} {to_unit}")

# Temperature Conversion

elif conversion_choice == "Temperature":
    temperature_units = ["Celsius","Fahrenheit","Kelvin"]
    input_value = st.number_input("Enter Temperature Value", min_value=0.0, format="%.2f")
    from_unit = st.selectbox("From Unit:", temperature_units)
    to_unit = st.selectbox("To Unit:", temperature_units)

    # Conversion Dictionaries

    def convert_temperature(value, from_unit, to_unit):
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32)*5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
        else:
            return value
    if st.button("Convert"):
        result = convert_temperature(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} = {result} {to_unit}")








