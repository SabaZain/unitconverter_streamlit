# Unit Converter Project
import streamlit as st
st.markdown("""
<style>
body {
    background-color: #B3AEAF;
    color: #000000;
}
.stApp {
    background-color: linear-gradient(to right, #00b09b, #96c93d);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
}
h1 {
    text-align: center;
    color: #000000;
}
.stButton {
    background-color: #EFC3CA;
    color: #3E2FDE;
    font-size: 16px;
    border-radius: 5px;
    padding: 10px;
    transition: background-color 0.3s ease;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
}
.stButton:hover {
    transform: scale(1.05);
    background-color: linear-gradient(to right, #00b09b, #96c93d);
    color: #000000; 
}
.result-box {
    text-align: center;
    color: #000000;
    font-size: 20px;
    font-weight: bold;
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.1);
}
.footer {
    text-align: center;
    color: #000000;
    font-size: 16px;
    font-weight: bold;
    margin-top: 20px;   
}   
</style>
""", unsafe_allow_html=True)

#Title and Description
st.markdown("<h1>Unit Converter Using Python and Streamlit</h1>", unsafe_allow_html=True)
st.write("**Easily convert between different units of length, weight, and temperature.**")

#sidebar menu
conversion_type = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)
col1, col2 = st.columns(2)

#length conversion
if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Inches", "Feet"])
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilograms", "Grams", "Milligrams", "Micrograms", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilograms", "Grams", "Milligrams", "Micrograms", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:  
        from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])

#converted function
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Inches": 39.3701,
        "Feet": 3.28084,
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Micrograms": 1000000000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value    
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value
    return value

# Button to convert 
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown(f"<div class='footer'>Created with ❤️ by Saba Ali Zain</div>", unsafe_allow_html=True)   

    

