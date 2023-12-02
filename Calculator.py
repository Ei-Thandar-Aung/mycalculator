import streamlit as st

st.title("Simple Calculator")

# Function to perform calculations
def calculator(num1, num2, operation):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = ""

    return result

# Sidebar for user input
st.sidebar.header("Calculator Settings")
num1 = st.sidebar.number_input("Enter the first number:")
num2 = st.sidebar.number_input("Enter the second number:")
operation = st.sidebar.selectbox("Select operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate and display result
if st.sidebar.button("Calculate"):
    result = calculator(num1, num2, operation)
    st.sidebar.success(f"Result: {result}")

st.write("Welcome to the Simple Calculator App!")
