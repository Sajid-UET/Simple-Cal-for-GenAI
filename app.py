# Install Streamlit if you haven't already
# !pip install streamlit

import streamlit as st

# Title of the app
st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")
operation = st.selectbox("Choose operation", ("+", "-", "*", "/"))

# Calculate result
if st.button("Calculate"):
    if operation == '+':
        result = num1 + num2
        st.write(f"The result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result = num1 - num2
        st.write(f"The result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result = num1 * num2
        st.write(f"The result of {num1} * {num2} is: {result}")
    elif operation == '/':
        if num2 == 0:
            st.write("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.write(f"The result of {num1} / {num2} is: {result}")
