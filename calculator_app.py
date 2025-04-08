import streamlit as st

st.title("🧮 Simple Calculator")
st.write("A beginner-friendly calculator app!")

num1 = st.number_input("Enter first number")
operator = st.selectbox("Select operation", ['+', '-', '*', '/'])
num2 = st.number_input("Enter second number")

if st.button("Calculate"):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    
    st.success(f"Result: {result}")