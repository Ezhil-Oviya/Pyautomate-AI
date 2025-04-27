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
    
    # Initialize display in session state if not already set
    if 'display' not in st.session_state:
        st.session_state.display = "0"
    
    # Basic mode: Simple calculator
    if mode == "Basic":
        st.subheader("Basic Calculator")
        
        # Calculator display area
        display = st.text_input("Display", st.session_state.display, key="display", disabled=True, label_visibility="collapsed")
        
        # Buttons layout
        cols = st.columns(4)
        button_labels = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
        ]
        
        # Capture button clicks
        for i, label in enumerate(button_labels):
            with cols[i % 4]:
                if st.button(label):
                    if st.session_state.display == "0":
                        st.session_state.display = label
                    else:
                        st.session_state.display += label

        # Action buttons
        if st.button("=", use_container_width=True):
            result = calculate(st.session_state.display)
            st.session_state.display = str(result)
        
        if st.button("Clear", use_container_width=True):
            st.session_state.display = "0"
    
    # Scientific mode: Advanced functions
    if mode == "Scientific":
        st.subheader("Scientific Calculator")

        # Calculator display area for scientific mode
        display = st.text_input("Display", st.session_state.display, key="display", disabled=True, label_visibility="collapsed")

        # Trigonometric functions input
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

        # Exponential function
        exp_number = st.number_input("Enter number for exponentiation", value=1.0)
        exp_result = st.number_input("Enter exponent", value=2)
        
        if st.button("Calculate Exponential", use_container_width=True):
            st.write(f"exp({exp_number}) = {math.exp(exp_number)}")
            st.write(f"{exp_number}^{exp_result} = {exp_number ** exp_result}")

        # Scientific expression input
        expression = st.text_input("Enter scientific expression (e.g., sin(30), 2+3, exp(2))")
        
        if expression:
            result = calculate(expression)
            st.write(f"Result: {result}")

if __name__ == "__main__":
    main()
