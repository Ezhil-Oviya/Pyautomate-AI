import streamlit as st
import math

# Function to perform calculations
def calculate(expression):
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

# Main function for the app
def main():
    st.title("Scientific Calculator")
    
    # Mode selection: Basic or Scientific
    mode = st.radio("Select Mode", ("Basic", "Scientific"))
    
    # Basic mode: Simple calculator
    if mode == "Basic":
        st.subheader("Basic Calculator")
        num1 = st.number_input("Enter first number", value=0.0)
        num2 = st.number_input("Enter second number", value=0.0)
        operation = st.selectbox("Select operation", ("+", "-", "*", "/"))
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        
        st.write(f"Result: {result}")

    # Scientific mode: Advanced functions
    if mode == "Scientific":
        st.subheader("Scientific Calculator")

        expression = st.text_input("Enter expression (e.g., 2+3, sin(30), cos(45), exp(2))")
        
        if expression:
            result = calculate(expression)
            st.write(f"Result: {result}")

        # Trigonometric Functions
        angle = st.number_input("Enter angle (in degrees)", value=0)
        angle_rad = math.radians(angle)
        
        trig_operations = ["sin", "cos", "tan", "asin", "acos", "atan"]
        trig_function = st.selectbox("Select Trigonometric function", trig_operations)
        
        if trig_function == "sin":
            st.write(f"sin({angle}) = {math.sin(angle_rad)}")
        elif trig_function == "cos":
            st.write(f"cos({angle}) = {math.cos(angle_rad)}")
        elif trig_function == "tan":
            st.write(f"tan({angle}) = {math.tan(angle_rad)}")
        elif trig_function == "asin":
            st.write(f"asin({angle}) = {math.degrees(math.asin(angle_rad))}")
        elif trig_function == "acos":
            st.write(f"acos({angle}) = {math.degrees(math.acos(angle_rad))}")
        elif trig_function == "atan":
            st.write(f"atan({angle}) = {math.degrees(math.atan(angle_rad))}")

        # Exponential Function
        exp_number = st.number_input("Enter number for exponentiation", value=1.0)
        exp_result = st.number_input("Enter exponent", value=2)
        if st.button("Calculate Exponential"):
            st.write(f"exp({exp_number}) = {math.exp(exp_number)}")
            st.write(f"{exp_number}^{exp_result} = {exp_number ** exp_result}")

if __name__ == "__main__":
    main()
